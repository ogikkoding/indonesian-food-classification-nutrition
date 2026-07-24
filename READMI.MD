# 🍽️ Klasifikasi Citra Makanan Indonesia Menggunakan Hybrid Transfer Learning ResNet50 dan Support Vector Machine (SVM)

> Sistem klasifikasi citra makanan khas Indonesia berbasis Web Streamlit menggunakan metode Hybrid Transfer Learning ResNet50 sebagai Feature Extractor dan Support Vector Machine (SVM) sebagai Classifier serta penyajian informasi nilai gizi secara otomatis.

---

# 📖 Deskripsi

Proyek ini bertujuan untuk membangun sistem klasifikasi citra makanan khas Indonesia menggunakan kombinasi metode **Deep Learning** dan **Machine Learning**.

Model **ResNet50** digunakan sebagai *feature extractor* untuk mengekstraksi fitur visual dari citra makanan, kemudian fitur tersebut diklasifikasikan menggunakan **Support Vector Machine (SVM)**.

Selain melakukan klasifikasi, sistem juga menampilkan informasi nilai gizi makanan secara otomatis berdasarkan database gizi Indonesia sehingga pengguna dapat mengetahui kandungan nutrisi dari makanan yang diprediksi.

---

# 🖼️ Tampilan Aplikasi

### Halaman Utama

> Tampilan awal aplikasi sebelum proses prediksi.

![Halaman Utama](images/home.png)

---

### Hasil Prediksi

> Hasil klasifikasi makanan beserta tingkat kepercayaan (Confidence Score).

![Prediksi](images/prediksi.png)

---

### Informasi Nilai Gizi

> Informasi energi, protein, lemak, dan karbohidrat yang ditampilkan secara otomatis.

![Nilai Gizi](images/gizi.png)

---

# ✨ Fitur

- 📤 Upload citra makanan Indonesia
- 🤖 Klasifikasi otomatis menggunakan ResNet50 + SVM
- 📊 Menampilkan Confidence Score
- 🥗 Menampilkan informasi nilai gizi
- 🔥 Menampilkan energi (kalori)
- 🥩 Menampilkan protein
- 🧈 Menampilkan lemak
- 🍚 Menampilkan karbohidrat
- 💾 Mengunduh hasil prediksi
- 🌐 Antarmuka berbasis Streamlit

---

# 🧠 Metode

## Deep Learning

- Transfer Learning
- ResNet50
- Feature Extraction

## Machine Learning

- StandardScaler
- Support Vector Machine (SVM)

---

# 🔄 Pipeline Sistem

```text
Dataset
    │
    ▼
Image Preprocessing
    │
    ▼
Transfer Learning ResNet50
    │
    ▼
Feature Extraction
    │
    ▼
Feature Vector
    │
    ▼
StandardScaler
    │
    ▼
Support Vector Machine
    │
    ▼
Prediksi Jenis Makanan
    │
    ▼
Pencarian Database Gizi
    │
    ▼
Informasi Nilai Gizi
    │
    ▼
Aplikasi Streamlit
```

---

## 🖼️ Diagram Pipeline

![Pipeline](images/pipeline.png)

---

# 🏗️ Arsitektur Sistem

```text
Citra Makanan
      │
      ▼
Image Preprocessing
      │
      ▼
ResNet50
      │
      ▼
Feature Extraction
      │
      ▼
Feature Vector
      │
      ▼
StandardScaler
      │
      ▼
Support Vector Machine
      │
      ▼
Prediksi
      │
      ▼
Database Nilai Gizi
      │
      ▼
Informasi Gizi
      │
      ▼
Web Streamlit
```

---

## 🖼️ Diagram Arsitektur

![Arsitektur](images/architecture.png)

---

# ⚙️ Alur Kerja Sistem

1. Pengguna mengunggah citra makanan.
2. Sistem melakukan preprocessing citra.
3. ResNet50 mengekstraksi fitur citra.
4. Feature vector dinormalisasi menggunakan StandardScaler.
5. Support Vector Machine melakukan klasifikasi.
6. Sistem mencari data gizi sesuai hasil prediksi.
7. Informasi nilai gizi ditampilkan kepada pengguna.

---

# 📂 Struktur Folder

```text
project/

├── STREAMLIT NILAI GIZI/
│   ├── app.py
│   └── run.bat
│
├── DATASET/
│   └── database_nilai_gizi_makanan_indonesia.xlsx
│
├── MODELS/
│   ├── svm_model.pkl
│   ├── scaler.pkl
│   └── class_indices.pkl
│
├── images/
│   ├── home.png
│   ├── prediksi.png
│   ├── gizi.png
│   ├── pipeline.png
│   ├── architecture.png
│   ├── dataset.png
│   └── output.png
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Teknologi yang Digunakan

- Python
- Streamlit
- PyTorch
- TIMM
- ResNet50
- Scikit-Learn
- Support Vector Machine (SVM)
- Pandas
- NumPy
- Pillow

---

# 📊 Dataset

Dataset yang digunakan berasal dari beberapa sumber untuk mendukung proses klasifikasi citra makanan Indonesia.

## Sumber Dataset

- Dataset Penelitian Makanan Indonesia (Kaggle)
- FatSecret Indonesia

### Database Nilai Gizi

Informasi yang digunakan meliputi:

- Energi
- Protein
- Lemak
- Karbohidrat

---

## 🖼️ Contoh Dataset

![Dataset](images/dataset.png)

---

# 📋 Hasil Keluaran Sistem

Sistem menghasilkan:

- Nama makanan
- Confidence Score
- Energi
- Protein
- Lemak
- Karbohidrat

---

## 🖼️ Contoh Hasil Sistem

![Output](images/output.png)

---

# 🚀 Cara Menjalankan Aplikasi

## Clone Repository

```bash
git clone https://github.com/username/project.git
```

## Install Library

```bash
pip install -r requirements.txt
```

## Menjalankan Streamlit

```bash
streamlit run app.py
```

---

# 💻 Platform Pengembangan

- Google Colab
- Google Drive
- Streamlit

---

# 👨‍💻 Pengembang

**Yogi Irawan**

🎓 Mahasiswa S1 Informatika

🤖 Bidang Minat: Artificial Intelligence & Computer Vision

📧 Email:
yogiirawan490@gmail.com

💼 LinkedIn:
https://www.linkedin.com/in/yogi-irawan-ab146a387

🐙 GitHub:
https://github.com/username

---

# 📄 Lisensi

Proyek ini dikembangkan untuk keperluan penelitian akademik dan pendidikan.