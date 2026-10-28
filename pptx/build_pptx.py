"""Bangun file PowerPoint cadangan dari index.html (satu sumber konten).

Jalankan dari root repo:  python pptx/build_pptx.py
Hasil: pptx/Seminar-Tren-Riset-AI.pptx
"""
import math
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "index.html"
OUT = ROOT / "pptx" / "Seminar-Tren-Riset-AI.pptx"

BG = RGBColor(0x0B, 0x14, 0x26)
CARD = RGBColor(0x17, 0x2A, 0x4A)
LINE = RGBColor(0x2A, 0x42, 0x68)
TEXT = RGBColor(0xE8, 0xEE, 0xF8)
MUTED = RGBColor(0x9F, 0xB2, 0xCF)
TEAL = RGBColor(0x2D, 0xD4, 0xBF)
ORANGE = RGBColor(0xFB, 0x92, 0x3C)
YELLOW = RGBColor(0xFA, 0xCC, 0x15)
BLUE = RGBColor(0x60, 0xA5, 0xFA)
FONT = "Plus Jakarta Sans"
MONO = "JetBrains Mono"

W, H = Inches(13.333), Inches(7.5)
MX = Inches(0.7)
CW = W - 2 * MX


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


def runs_of(el):
    """Ubah elemen HTML menjadi daftar (teks, warna) agar <strong>/<em> tetap berwarna."""
    out = []
    for node in el.children:
        if isinstance(node, NavigableString):
            out.append((str(node), None))
        elif node.name == "br":
            out.append(("\n", None))
        elif node.name in ("strong", "b"):
            out.append((node.get_text(), TEAL))
        elif node.name == "em":
            out.append((node.get_text(), ORANGE))
        elif node.name == "cite":
            continue
        else:
            out.extend(runs_of(node))
    merged = "".join(t for t, _ in out)
    if not merged.strip():
        return []
    # rapikan spasi tanpa menghilangkan pemisah antar-run
    res = []
    for t, c in out:
        t = re.sub(r"[ \t\r\f\v]*\n[ \t\r\f\v]*", "\n", re.sub(r"[ \t\r\f\v\n]+(?!\n)", " ", t)) if t != "\n" else t
        res.append((t, c))
    res[0] = (res[0][0].lstrip(), res[0][1])
    res[-1] = (res[-1][0].rstrip(), res[-1][1])
    return res


def add_text(slide, x, y, w, h, runs, size=18, color=TEXT, bold=False, font=FONT,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    if isinstance(runs, str):
        runs = [(runs, None)]
    p = tf.paragraphs[0]
    p.alignment = align
    for text, c in runs:
        parts = text.split("\n")
        for i, part in enumerate(parts):
            if i:
                p = tf.add_paragraph()
                p.alignment = align
            if not part:
                continue
            r = p.add_run()
            r.text = part
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.name = font
            r.font.color.rgb = c or color
    return tb


def add_box(slide, x, y, w, h, border=LINE, fill=CARD, radius=0.08):
    s = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    s.adjustments[0] = radius
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    s.line.color.rgb = border
    s.line.width = Pt(1.25)
    s.shadow.inherit = False
    return s


def text_height(text, width_in, size):
    chars_per_line = max(8, int(width_in * 72 / (size * 0.58)))
    lines = sum(max(1, math.ceil(len(seg) / chars_per_line)) for seg in text.split("\n"))
    return lines * size * 1.3 / 72


def border_of(classes):
    if "hl" in classes:
        return TEAL
    if "warn" in classes:
        return ORANGE
    return LINE


def render_cards(slide, grid, y):
    cards = grid.find_all("div", class_="card", recursive=False)
    cls = grid.get("class", [])
    cols = 4 if "g4" in cls else 3 if "g3" in cls else 2
    if len(cards) == 1:
        cols = 1
    gap = Inches(0.22)
    cw = (CW - gap * (cols - 1)) / cols
    rows = math.ceil(len(cards) / cols)
    w_in = cw / 914400 - 0.3
    row_h = []
    for r in range(rows):
        hh = 0
        for c in cards[r * cols:(r + 1) * cols]:
            hh = max(hh, card_height(c, w_in))
        row_h.append(hh)
    for i, c in enumerate(cards):
        r, k = divmod(i, cols)
        x = MX + (cw + gap) * k
        yy = y + Inches(sum(row_h[:r])) + gap * r
        draw_card(slide, c, x, yy, cw, Inches(row_h[r]))
    return y + Inches(sum(row_h)) + gap * (rows - 1)


def card_height(card, w_in):
    h = 0.3
    for el in card.find_all(["span", "h3", "p", "div"], recursive=False):
        if el.name == "div" and "flow" in el.get("class", []):
            h += 0.75
            continue
        size = 12 if el.name == "span" else 18 if el.name == "h3" else 15
        h += text_height(clean(el.get_text()), w_in, size) + 0.05
    return h


def draw_card(slide, card, x, y, w, h):
    add_box(slide, x, y, w, h, border_of(card.get("class", [])))
    cy = y + Inches(0.15)
    iw = w - Inches(0.3)
    w_in = iw / 914400
    for el in card.find_all(["span", "h3", "p", "div"], recursive=False):
        if el.name == "div" and "flow" in el.get("class", []):
            render_flow(slide, el, cy, x0=x + Inches(0.15), width=iw, height=Inches(0.65), size=12)
            cy += Inches(0.75)
            continue
        txt = clean(el.get_text())
        if el.name == "span":
            add_text(slide, x + Inches(0.15), cy, iw, Inches(0.3), txt.upper(), 12, TEAL, font=MONO)
            hh = text_height(txt, w_in, 12)
        elif el.name == "h3":
            add_text(slide, x + Inches(0.15), cy, iw, Inches(0.4), runs_of(el), 18, TEXT, bold=True)
            hh = text_height(txt, w_in, 18)
        else:
            add_text(slide, x + Inches(0.15), cy, iw, Inches(0.5), runs_of(el), 15, MUTED)
            hh = text_height(txt, w_in, 15)
        cy += Inches(hh + 0.05)


def render_flow(slide, flow, y, x0=MX, width=CW, height=None, size=15):
    boxes = flow.find_all("div", recursive=False)
    n = len(boxes)
    arrow = Inches(0.35)
    bw = (width - arrow * (n - 1)) / n
    if height is None:
        w_in = bw / 914400 - 0.2
        height = Inches(max(text_height(clean(b.get_text(" ")), w_in, size) for b in boxes) + 0.45)
    for i, b in enumerate(boxes):
        x = x0 + (bw + arrow) * i
        add_box(slide, x, y, bw, height)
        head = b.find("b")
        runs = []
        if head:
            runs.append((clean(head.get_text()) + "\n", TEAL))
            rest = clean(" ".join(str(t) if isinstance(t, NavigableString) else t.get_text(" ")
                                  for t in b.children if t is not head))
        else:
            rest = clean(b.get_text(" "))
        runs.append((rest, TEXT))
        add_text(slide, x + Inches(0.05), y, bw - Inches(0.1), height, runs, size,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        if i < n - 1:
            add_text(slide, x + bw, y, arrow, height, "→", size + 6, TEAL,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    return y + height


def render_timeline(slide, tl, y):
    items = tl.find_all("div", recursive=False)
    n = len(items)
    seg = CW / n
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, MX, y + Inches(0.2), MX + CW, y + Inches(0.2))
    line.line.color.rgb = TEAL
    line.line.width = Pt(3)
    for i, it in enumerate(items):
        cx = MX + seg * i + seg / 2
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.13), y + Inches(0.07), Inches(0.26), Inches(0.26))
        dot.fill.solid()
        dot.fill.fore_color.rgb = BG
        dot.line.color.rgb = TEAL
        dot.line.width = Pt(3)
        year = clean(it.find("b").get_text())
        rest = clean(it.get_text(" ").replace(it.find("b").get_text(), "", 1))
        add_text(slide, cx - seg / 2, y + Inches(0.45), seg, Inches(1.2),
                 [(year + "\n", ORANGE), (rest, TEXT)], 14, align=PP_ALIGN.CENTER)
    return y + Inches(1.6)


def render_table(slide, table, y):
    rows = table.find_all("tr")
    ncol = max(len(r.find_all(["th", "td"])) for r in rows)
    rh = Inches(0.48)
    shape = slide.shapes.add_table(len(rows), ncol, MX, y, CW, rh * len(rows))
    tbl = shape.table
    if ncol == 3:
        widths = [0.18, 0.41, 0.41]
    else:
        widths = [0.3, 0.7]
    for i, f in enumerate(widths):
        tbl.columns[i].width = Emu(int(CW * f))
    for r, row in enumerate(rows):
        for c, cell in enumerate(row.find_all(["th", "td"])):
            tc = tbl.cell(r, c)
            tc.fill.solid()
            tc.fill.fore_color.rgb = CARD if r == 0 else BG
            tf = tc.text_frame
            tf.text = ""
            run = tf.paragraphs[0].add_run()
            run.text = clean(cell.get_text())
            run.font.size = Pt(16)
            run.font.name = FONT
            run.font.bold = cell.name == "th"
            run.font.color.rgb = TEAL if cell.name == "th" else (MUTED if c == 0 else TEXT)
    return y + rh * len(rows)


def render_concentric(slide, y):
    specs = [("Artificial Intelligence", BLUE, 4.6, 0.0), ("Machine Learning", TEAL, 3.5, 0.55),
             ("Deep Learning", ORANGE, 2.4, 1.1), ("Generative AI / LLM", YELLOW, 1.3, 1.65)]
    cx = MX + Inches(2.4)
    for label, col, d, _ in specs:
        top = y + Inches((4.6 - d) * 0.75)
        o = slide.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(d / 2), top, Inches(d), Inches(d))
        o.fill.solid()
        o.fill.fore_color.rgb = CARD
        o.line.color.rgb = col
        o.line.width = Pt(2.5)
        ty = top + Inches(0.15) if d > 1.5 else top + Inches(d / 2 - 0.3)
        add_text(slide, cx - Inches(d / 2), ty, Inches(d), Inches(0.5), label, 15 if d > 1.5 else 12,
                 col, bold=True, align=PP_ALIGN.CENTER)
    return y + Inches(4.8)


def render_agent_loop(slide, y):
    bw, bh = Inches(2.6), Inches(1.0)
    left, right = MX + Inches(0.4), MX + CW - Inches(3.0)
    for x, label, col in ((left, "Agent", TEAL), (right, "Environment", ORANGE)):
        add_box(slide, x, y, bw, bh, border=col)
        add_text(slide, x, y, bw, bh, label, 24, TEXT, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    for yy, col, label, start, end in ((y + Inches(0.3), TEAL, "aksi →", left + bw, right),
                                       (y + Inches(0.7), ORANGE, "← state baru + reward", right, left + bw)):
        ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, start, yy, end, yy)
        ln.line.color.rgb = col
        ln.line.width = Pt(2.5)
        ty = yy - Inches(0.42) if col == TEAL else yy + Inches(0.05)
        add_text(slide, left + bw, ty, right - left - bw, Inches(0.35), label, 16, col, align=PP_ALIGN.CENTER)
    return y + bh + Inches(0.2)


def render_profile(slide, prof, y):
    d = Inches(2.4)
    o = slide.shapes.add_shape(MSO_SHAPE.OVAL, MX, y + Inches(0.3), d, d)
    o.fill.solid()
    o.fill.fore_color.rgb = TEAL
    o.line.fill.background()
    add_text(slide, MX, y + Inches(0.3), d, d, "RIK", 54, BG, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    info = prof.find_all("div", recursive=False)[1]
    x = MX + d + Inches(0.5)
    w = CW - d - Inches(0.5)
    add_text(slide, x, y, w, Inches(0.7), clean(info.find("h2").get_text()), 36, TEXT, bold=True)
    add_text(slide, x, y + Inches(0.7), w, Inches(0.4), clean(info.find("p").get_text()), 16, MUTED)
    cy = y + Inches(1.2)
    for row in info.find("div", class_="edu").find_all("div", recursive=False):
        lvl = clean(row.find("b").get_text())
        rest = clean(row.get_text(" ").replace(lvl, "", 1))
        add_text(slide, x, cy, w, Inches(0.38), [(lvl + "   ", ORANGE), (rest, TEXT)], 17)
        cy += Inches(0.4)
    pills = [clean(p.get_text()) for p in info.find_all("span", class_="pill")]
    add_text(slide, x, cy + Inches(0.15), w, Inches(0.8), "   ·   ".join(pills), 13, TEAL, font=MONO)
    return y + Inches(3.2)


def build():
    soup = BeautifulSoup(SRC.read_text(encoding="utf-8"), "html.parser")
    sections = soup.select("div.slides > section")
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    blank = prs.slide_layouts[6]

    for sec in sections:
        s = prs.slides.add_slide(blank)
        s.background.fill.solid()
        s.background.fill.fore_color.rgb = BG

        act = sec.find("span", class_="act", recursive=False)
        if act:
            add_text(s, W - Inches(4.2), Inches(0.2), Inches(3.9), Inches(0.3), clean(act.get_text()),
                     11, MUTED, font=MONO, align=PP_ALIGN.RIGHT)

        blocks = [c for c in sec.children if getattr(c, "name", None)
                  and not ({"act", "notes", "src"} & set(c.get("class", []))) and c.name != "aside"]

        y = Inches(0.75)
        first_body = len(s.shapes)
        is_title = "title-slide" in sec.get("class", [])
        if is_title:
            y = Inches(1.6)

        for el in blocks:
            cls = el.get("class", [])
            if el.name == "span" and "kicker" in cls:
                add_text(s, MX, y, CW, Inches(0.3), clean(el.get_text()).upper(), 13, ORANGE, font=MONO)
                y += Inches(0.4)
            elif el.name == "h1":
                add_text(s, MX, y, CW, Inches(1.6), runs_of(el), 48, TEXT, bold=True)
                y += Inches(1.8)
            elif el.name == "h2":
                txt = clean(el.get_text())
                add_text(s, MX, y, CW, Inches(0.8), runs_of(el), 32, TEXT, bold=True)
                y += Inches(text_height(txt, CW / 914400, 32) + 0.25)
            elif el.name == "p":
                txt = clean(el.get_text(" ")) + "\n" * len(el.find_all("br"))
                align = PP_ALIGN.CENTER if "center" in cls else PP_ALIGN.LEFT
                if "quote" in cls:
                    size = 30 if len(txt) < 80 else 24
                    runs = runs_of(el)
                    cite = el.find("cite")
                    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, MX, y, Inches(0.08),
                                             Inches(text_height(txt, 11.5, size) + (0.4 if cite else 0)))
                    bar.fill.solid()
                    bar.fill.fore_color.rgb = ORANGE
                    bar.line.fill.background()
                    hh = text_height(txt, 11.5, size)
                    add_text(s, MX + Inches(0.3), y, CW - Inches(0.3), Inches(hh), runs, size, TEXT, bold=True)
                    y += Inches(hh)
                    if cite:
                        add_text(s, MX + Inches(0.3), y, CW, Inches(0.35), clean(cite.get_text()), 14, MUTED)
                        y += Inches(0.4)
                    y += Inches(0.25)
                else:
                    size = 34 if "big" in cls else 22 if "lead" in cls else 16
                    if "big" in cls and "font-size" in el.get("style", ""):
                        size = 26
                    color = MUTED if ("lead" in cls or "muted" in cls or "who" in cls) else TEXT
                    hh = text_height(txt, CW / 914400, size)
                    add_text(s, MX, y, CW, Inches(hh), runs_of(el), size, color, bold="big" in cls, align=align)
                    y += Inches(hh + 0.2)
            elif el.name == "div" and "grid" in cls:
                if el.find("svg"):
                    render_concentric(s, y)
                    side = el.find_all("div", recursive=False)[0]
                    yy = y + Inches(1.0)
                    for p in side.find_all("p"):
                        add_text(s, MX + Inches(5.6), yy, CW - Inches(5.6), Inches(0.7), runs_of(p), 19, TEXT)
                        yy += Inches(0.75)
                    y += Inches(4.9)
                else:
                    y = render_cards(s, el, y) + Inches(0.25)
            elif el.name == "div" and "card" in cls:
                g = soup.new_tag("div", attrs={"class": "grid"})
                g.append(el.__copy__())
                y = render_cards(s, g, y) + Inches(0.25)
            elif el.name == "div" and "flow" in cls:
                y = render_flow(s, el, y) + Inches(0.3)
            elif el.name == "div" and "timeline" in cls:
                y = render_timeline(s, el, y) + Inches(0.2)
            elif el.name == "div" and "profile" in cls:
                y = render_profile(s, el, y)
            elif el.name == "table":
                y = render_table(s, el, y) + Inches(0.25)
            elif el.name == "svg":
                y = render_agent_loop(s, y) + Inches(0.2)

        # pusatkan isi secara vertikal seperti versi HTML
        free = H - Inches(0.8) - y
        if free > 0:
            shift = int(free / 2) if not is_title else 0
            for shp in list(s.shapes)[first_body:]:
                shp.top = shp.top + shift

        src = sec.find("p", class_="src", recursive=False)
        if src:
            add_text(s, MX, H - Inches(0.6), CW - Inches(1.2), Inches(0.45), clean(src.get_text()), 10, MUTED)
        add_text(s, W - Inches(1.3), H - Inches(0.5), Inches(0.9), Inches(0.3),
                 f"{len(prs.slides)}/{len(sections)}", 10, MUTED, font=MONO, align=PP_ALIGN.RIGHT)

        notes = sec.find("aside", class_="notes")
        if notes:
            s.notes_slide.notes_text_frame.text = clean(notes.get_text())

    OUT.parent.mkdir(exist_ok=True)
    prs.save(OUT)
    print(f"Tersimpan: {OUT.relative_to(ROOT)} ({len(prs.slides)} slide)")


if __name__ == "__main__":
    build()
