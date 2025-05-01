[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=900&size=33&pause=1000&color=F71A58&background=FB16EE00&width=440&lines=NgOCR-in)](https://git.io/typing-svg)

# ✨ NgOCR-in v2.0

OCR (Optical Character Recognition) cerdas dengan dukungan multi-bahasa, auto-translate opsional, dan ekspor hasil ke `.txt` & `.docx`. Dirancang dengan tampilan terminal interaktif, penuh warna, dan dukungan untuk drag & drop dari Windows ke WSL/Linux.

---

### 📸 Tampilan Tools

![NgOCR-in Screenshot](https://i.imgur.com/8k4eAiU.png)

---

### 🚀 Fitur Utama

- Dukungan OCR berbagai bahasa (Latin, Jepang, Korea, Arab, China, dll)
- Deteksi otomatis bahasa gambar (auto-detect)
- Translate opsional ke berbagai bahasa
- Output hasil ke `.txt` dan `.docx`
- Tampilan terminal dengan warna yang menarik
- Mendukung batch processing (OCR banyak gambar sekaligus)
- Bisa drag & drop path file dari Windows ke WSL/Linux

---

### ⚙️ Instalasi

#### 1. Clone Repositori
```bash
git clone https://github.com/rivaile96/NgOCR-in.git
cd NgOCR-in
```

#### 2. Buat & Aktifkan Virtual Environment
```bash
python3 -m venv ocr-env
source ocr-env/bin/activate  # atau gunakan .\ocr-env\Scripts\activate di Windows
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Install Tesseract dan Font (Linux/WSL)
```bash
sudo apt update
sudo apt install tesseract-ocr-all
sudo apt install fonts-dejavu-core fonts-liberation fonts-freefont-ttf
```
> *Instalasi font ini penting agar hasil OCR tidak menjadi simbol aneh atau rusak.*

---

### ▶️ Menjalankan Tools

```bash
python3 main.py
```

- Pilih mode OCR (Gambar tunggal atau folder/batch)
- Pilih bahasa OCR atau gunakan Auto-Detect
- Masukkan path gambar (bisa drag & drop ke terminal)
- Pilih PSM (Page Segmentation Mode, default: 6)
- Hasil OCR akan tampil, dan bisa dipilih untuk diterjemahkan atau tidak
- Simpan hasil jika diinginkan (otomatis simpan ke `ocr_result.txt` dan `ocr_result.docx`)

---

### 📦 Struktur Output

```
📁 NgOCR-in
├── ocr_result.txt       # Hasil OCR & terjemahan dalam format teks
├── ocr_result.docx      # Hasil OCR & terjemahan dalam format dokumen
```

---

### 📌 Catatan Tambahan

- Gunakan `fonts` yang mendukung banyak karakter agar hasil OCR maksimal.
- Beberapa bahasa memerlukan model khusus, pastikan `tesseract-ocr-all` telah terinstal.
- Pastikan Python 3.8+ telah terinstal.
- Rekomendasi terminal: Windows Terminal / Terminator / Tilix agar warna tampil sempurna.

---

### 👨‍💻 Author

**Rivaile**  
NgOCR-in - v2.0 ❤️  

---

> Feel free to fork, improve, and share. Let's OCR the world! 🌍

