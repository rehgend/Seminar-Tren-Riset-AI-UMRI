# Seminar Tren Riset AI — UMRI

Presentasi **"Tren Riset Informatika Masa Kini dan Masa Mendatang (Bidang Kecerdasan Buatan)"**
oleh Rahman Indra Kesuma (Teknik Informatika, Institut Teknologi Sumatera).

Sesi 90 menit: ±60 menit pemaparan (34 slide) + ±30 menit tanya jawab.
Big idea: **"Mulai dari masalah, bukan dari model."**

## Isi repo

| Path | Keterangan |
|---|---|
| `index.html` | Deck utama (reveal.js), siap untuk GitHub Pages |
| `assets/css/theme.css` | Tema visual deck |
| `docs/kerangka-presentasi.md` | Tujuan, big idea, angle, alokasi waktu, outline, referensi |
| `pptx/Seminar-Tren-Riset-AI.pptx` | Cadangan PowerPoint (dengan speaker notes) |
| `pptx/build_pptx.py` | Membangun ulang PPTX dari `index.html` |

## Menjalankan

Buka lokal:

```bash
python3 -m http.server 8000
```

Lalu buka `http://localhost:8000`. Perlu koneksi internet untuk memuat reveal.js dan font.

Pintasan saat presentasi: `→`/`Spasi` slide berikutnya, `S` speaker view (naskah + timer), `F` layar penuh, `Esc` ikhtisar slide.
Ekspor PDF: buka `index.html?print-pdf` di Chrome, lalu cetak ke PDF.

## GitHub Pages

Settings → Pages → *Build and deployment* → Source: **Deploy from a branch** → pilih branch dan folder `/ (root)` → Save.
Deck akan tersedia di `https://<username>.github.io/Seminar-Tren-Riset-AI-UMRI/`.

## Memperbarui PPTX

Setelah mengubah `index.html`:

```bash
pip install python-pptx beautifulsoup4
```

```bash
python pptx/build_pptx.py
```
