# Kerangka Presentasi
**Tren Riset Informatika Masa Kini dan Masa Mendatang (Bidang Kecerdasan Buatan)**
Narasumber: Rahman Indra Kesuma — Teknik Informatika, Institut Teknologi Sumatera

## 1. Desain inti

| Elemen | Isi |
|---|---|
| **Tujuan utama** | Mahasiswa memahami peta AI (AI → ML → DL → LLM → Multimodal → Agentic) dan mampu menerjemahkan satu masalah nyata di sekitarnya (Riau/Sumatera) menjadi rencana riset/skripsi AI dengan research gap yang jelas. |
| **Satu ide yang harus diingat** | **"Mulai dari masalah, bukan dari model."** AI hanyalah alat; riset bernilai lahir dari masalah nyata di sekitar kita, dikerjakan dengan pikiran yang tetap kritis. |
| **Sudut pandang (angle)** | *Perjalanan tiga babak*: **Peta** (memahami AI) → **Gelombang** (tren riset) → **Kompas** (peluang, etika, cara meneliti). Satu studi kasus benang merah — **kebakaran hutan & lahan (karhutla) Riau** — "naik level" di setiap babak: CNN mendeteksi asap → model sekuensial memprediksi hotspot → multimodal menggabungkan satelit, sensor, dan laporan warga → agent memantau dan memberi peringatan. |
| **Jumlah slide** | **37 slide** (34 slide materi + 3 slide Ruang Diskusi) untuk ±60 menit pemaparan, lalu 30 menit tanya jawab. Total sesi 90 menit. |
| **Prinsip visual** | Satu pesan per slide, maksimal ±25 kata, diagram menggantikan paragraf, kutipan sumber kecil di kaki slide. Naskah lengkap ada di speaker notes (tekan `S`). |

## 2. Alur dan alokasi waktu

| Bagian | Slide | Waktu | Fungsi dalam cerita |
|---|---|---|---|
| Pembuka | 1–5 | 5' | Hook ("Berapa kali kamu pakai AI hari ini?", 05.30–22.30), perkenalan narasumber, peta perjalanan, big idea |
| Babak 1 — Peta | 6–16 | 16' | Definisi AI, sejarah, AI ⊃ ML ⊃ DL ⊃ GenAI, empat keluarga arsitektur DL beserta contoh nyata, rangkuman "satu masalah, empat cara pandang", **Ruang Diskusi 1** |
| Babak 2 — Gelombang | 17–28 | 18' | LLM (mengapa tren, cara kerja, arsitektur, tantangan), Multimodal AI (mengapa, cara kerja, pendekatan, penerapan), Agentic AI (vs GenAI, anatomi & cara belajar, tools), benang merah 4 level, **Ruang Diskusi 2** |
| Babak 3 — Kompas | 29–36 | 19' | Peluang di Riau & Sumatera, empat pilar AI bertanggung jawab, **Ruang Diskusi 3**, empat jebakan kognitif + penangkal, research gap, rumus skripsi S1, peta jalan 6 langkah |
| Penutup | 37 | 2' | Quote, kembali ke big idea dan pertanyaan pembuka |
| Tanya jawab | — | 30' | Diskusi |

## 3. Outline per slide

**Pembuka**
1. Judul
2. Hook: sehari bersama AI, dari bangun tidur sampai menjelang tidur (belajar, mobilitas, hiburan), ditutup pertanyaan benang merah kabut asap Riau
3. Profil narasumber: pendidikan (Unila → UGM → ITB), mata kuliah yang diampu
4. Fokus riset: Human Activity Recognition dari video domain kriminalitas + publikasi terpilih
5. Peta perjalanan tiga babak + big idea

**Babak 1 — Peta**
6. Definisi AI (McCarthy; 4 pendekatan Russell & Norvig; rational agent)
7. Timeline AI: 1956 → AI Winter → 2012 AlexNet → 2017 Transformer → 2022 ChatGPT → 2025+ Agentic
8. Diagram AI ⊃ ML ⊃ DL ⊃ GenAI
9. ML klasik vs DL: siapa yang merancang fitur?
10. Empat keluarga arsitektur DL (melihat, mengingat urutan, mencoba, mencipta)
11. Deep Computer Vision: CNN, ResNet, YOLO, U-Net, ViT — deteksi asap, penyakit daun sawit, CCTV
12. Deep Sequential Model: RNN, LSTM, GRU, Transformer — prediksi hotspot, harga TBS, speech-to-text
13. Deep Reinforcement Learning: DQN, PPO, AlphaGo — lalu lintas, robot, drone, RLHF
14. Deep Generative Network: VAE, GAN, Diffusion — augmentasi data, text-to-image, deepfake
15. Rangkuman: satu masalah karhutla, empat cara pandang
16. **Ruang Diskusi 1 — Asap atau awan?** Dua ilustrasi citra satelit; peserta menebak mana yang asap, menyebut petunjuk visual (fitur), dan merancang data/label untuk CNN (3')

**Babak 2 — Gelombang**
17. LLM: mengapa jadi pusat riset (scaling laws, serba bisa, foundation model)
18. Cara kerja LLM: tokenisasi → embedding → self-attention → prediksi token berikutnya
19. Arsitektur: encoder/decoder/encoder-decoder; pre-training → SFT → RLHF/DPO
20. Tantangan (halusinasi, biaya, bias, low-resource language, evaluasi, keamanan) & penerapan (RAG, IndoBERT, SEA-LION)
21. Multimodal AI: mengapa dibutuhkan
22. Cara kerja: early/late/intermediate fusion; CLIP, LLaVA, GPT-4o/Gemini
23. Penerapan multimodal: kesehatan, pertanian, aksesibilitas, kebencanaan
24. Generative AI vs Agentic AI (tabel)
25. Anatomi agent & cara belajar: persepsi–penalaran–aksi–refleksi; ReAct, Reflexion, memori, multi-agent
26. Tools agentic: LangGraph, CrewAI, AutoGen, MCP, n8n, Claude Code, Copilot, Ollama
27. Benang merah: karhutla level 1–4
28. **Ruang Diskusi 2 — Yakin, tapi benarkah?** Mockup chat AI yang memberi referensi fiktif ber-DOI lalu agent mengirimnya ke dosen; bahas verifikasi, penyebab halusinasi, dan tanggung jawab (3')

**Babak 3 — Kompas**
29. Peluang AI di Riau & Sumatera: industri, pendidikan, masyarakat (+ sumber data terbuka)
30. Empat pilar: etika, keamanan, privasi (UU PDP), kehandalan
31. **Ruang Diskusi 3 — Kamera AI di kampus: setuju?** Frame CCTV dengan label "mencurigakan"; voting setuju/bersyarat/tidak, bahas bias dan rancang pengaman (4')
32. Empat jebakan: Cognitive Atrophy, Illusion of Competence, Erosion of Curiosity & Agency, Ethical Anaesthesia
33. Penangkal: AI sebagai sparring partner, bukan joki
34. Lima jenis research gap + cara cepat (Limitation & Future Work) + tools literatur
35. Rumus skripsi AI: masalah nyata + data + metode + evaluasi terukur; checklist standar S1
36. Peta jalan 6 langkah: dari ide ke publikasi

**Penutup**
37. Quote Alan Kay + pesan penutup + big idea + kontak

### Quote cadangan
- "AI is the new electricity." — Andrew Ng
- "The best way to predict the future is to invent it." — Alan Kay *(dipakai)*
- "AI is made by humans, intended to behave by humans, and ultimately to impact humans' lives." — Fei-Fei Li

## 4. Referensi

**Buku**
- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
- Jurafsky, D., & Martin, J. H. *Speech and Language Processing* (3rd ed. draft).

**Paper ilmiah**
- LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature*, 521, 436–444.
- Krizhevsky, A., Sutskever, I., & Hinton, G. (2012). ImageNet classification with deep CNNs. *NeurIPS*.
- He, K., dkk. (2016). Deep residual learning for image recognition. *CVPR*.
- Redmon, J., dkk. (2016). You Only Look Once. *CVPR*.
- Dosovitskiy, A., dkk. (2021). An image is worth 16x16 words (ViT). *ICLR*.
- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*.
- Cho, K., dkk. (2014). Learning phrase representations using RNN encoder–decoder. *EMNLP*.
- Mnih, V., dkk. (2015). Human-level control through deep RL. *Nature*.
- Silver, D., dkk. (2016). Mastering the game of Go. *Nature*.
- Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. *ICLR*.
- Goodfellow, I., dkk. (2014). Generative adversarial nets. *NeurIPS*.
- Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. *NeurIPS*.
- Vaswani, A., dkk. (2017). Attention is all you need. *NeurIPS*.
- Devlin, J., dkk. (2019). BERT. *NAACL*.
- Raffel, C., dkk. (2020). Exploring the limits of transfer learning (T5). *JMLR*.
- Kaplan, J., dkk. (2020). Scaling laws for neural language models. arXiv:2001.08361.
- Bommasani, R., dkk. (2021). On the opportunities and risks of foundation models. arXiv:2108.07258.
- Ouyang, L., dkk. (2022). Training language models to follow instructions with human feedback. *NeurIPS*.
- Rafailov, R., dkk. (2023). Direct preference optimization. *NeurIPS*.
- Lewis, P., dkk. (2020). Retrieval-augmented generation. *NeurIPS*.
- Ji, Z., dkk. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*.
- Wilie, B., dkk. (2020). IndoNLU. *AACL-IJCNLP*.
- Baltrušaitis, T., Ahuja, C., & Morency, L.-P. (2019). Multimodal machine learning: a survey and taxonomy. *IEEE TPAMI*.
- Radford, A., dkk. (2021). Learning transferable visual models from natural language supervision (CLIP). *ICML*.
- Liu, H., dkk. (2023). Visual instruction tuning (LLaVA). *NeurIPS*.
- Gemini Team (2023). Gemini: a family of highly capable multimodal models. arXiv:2312.11805.
- Yao, S., dkk. (2023). ReAct: synergizing reasoning and acting in language models. *ICLR*.
- Shinn, N., dkk. (2023). Reflexion. *NeurIPS*.
- Park, J. S., dkk. (2023). Generative agents. *UIST*.
- Wang, L., dkk. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science*.
- Kosmyna, N., dkk. (2025). Your brain on ChatGPT: accumulation of cognitive debt. MIT Media Lab, arXiv:2506.08872.
- Gerlich, M. (2025). AI tools in society: impacts on cognitive offloading and critical thinking. *Societies*, 15(1).
- Bjork, R. A., Dunlosky, J., & Kornell, N. (2013). Self-regulated learning: beliefs, techniques, and illusions. *Annual Review of Psychology*.
- Kitchenham, B. (2007). Guidelines for performing systematic literature reviews in software engineering.
- Page, M. J., dkk. (2021). The PRISMA 2020 statement. *BMJ*.

**Website & dokumen kebijakan**
- Stanford HAI — AI Index Report 2025 (hai.stanford.edu/ai-index)
- MIT 6.S191 Introduction to Deep Learning (introtodeeplearning.com)
- Strategi Nasional Kecerdasan Artifisial Indonesia 2020–2045 (ai-innovation.id)
- UNESCO (2021). Recommendation on the Ethics of Artificial Intelligence
- NIST (2023). AI Risk Management Framework 1.0
- UU RI No. 27 Tahun 2022 tentang Pelindungan Data Pribadi
- Sumber data: NASA FIRMS, SiPongi KLHK, BPS Provinsi Riau, Copernicus Sentinel-2

## 5. Catatan untuk narasumber
- Profil SINTA (ID 6647166) tidak dapat diakses secara otomatis saat deck dibuat. Publikasi di slide 4 diambil dari Garuda/jurnal (ICETD 2012, SENATIK 2018, IJISTECH 2021). **Perbarui slide 4 dengan publikasi, penelitian, dan HKI terbaru dari SINTA sebelum presentasi**, lalu jalankan ulang `python pptx/build_pptx.py`.
- Avatar "RIK" di slide 3 dapat diganti dengan foto: letakkan `assets/img/foto.jpg` dan ganti `<div class="avatar">RIK</div>` menjadi `<img class="avatar" src="assets/img/foto.jpg" alt="">`.
