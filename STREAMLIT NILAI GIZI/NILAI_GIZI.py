# ============================================================
# SISTEM KLASIFIKASI CITRA MAKANAN INDONESIA
# Hybrid Transfer Learning ResNet50 + Support Vector Machine
# ============================================================
import os
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import torch
import timm
from PIL import Image
from timm.data import resolve_model_data_config
from timm.data.transforms_factory import create_transform

# ============================================================
# KONFIGURASI HALAMAN (HARUS DIPANGGIL PERTAMA KALI)
# ============================================================
st.set_page_config(
    page_title="Klasifikasi Makanan Indonesia",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# LOKASI FOLDER DYNAMIC (ROOT REPOSITORY)
# ============================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "MODELS")
DATASET_DIR = os.path.join(BASE_DIR, "DATASET")

# ============================================================
# CSS CUSTOM MODERN
# ============================================================
st.markdown("""
<style>

/* Background App */
.stApp {
    background: linear-gradient(135deg, #0F172A, #111827, #000000);
}

/* Header Container Background (Hijau Modern) */
.header-container {
    background: linear-gradient(135deg, rgba(0, 137, 123, 0.15), rgba(38, 166, 154, 0.05));
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(38, 166, 154, 0.25);
    box-shadow: 0px 8px 25px rgba(0, 137, 123, 0.15);
    backdrop-filter: blur(10px);
    margin-bottom: 25px;
}

/* Main Title */
.main-title {
    text-align: center;
    color: #26A69A;
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 8px;
    letter-spacing: 1px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    color: #9CA3AF;
    font-size: 18px;
    margin-bottom: 0px;
}

/* Card */
.box {
    background: #1E293B;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2);
}

/* Result Card */
.result-box {
    background: linear-gradient(135deg, #064E3B, #022C22);
    padding: 25px;
    border-radius: 20px;
    border-left: 8px solid #10B981;
    box-shadow: 0px 10px 20px rgba(16, 185, 129, 0.15);
}

/* Metric Box */
.metric-box {
    background: #1E293B;
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #26A69A, #00897B);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 17px;
    font-weight: bold;
    padding: 12px;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #00897B, #00695C);
    transform: scale(1.02);
}

/* File Uploader */
[data-testid="stFileUploader"] {
    border: 2px dashed #00897B;
    border-radius: 15px;
    padding: 20px;
    background: rgba(15, 23, 42, 0.6);
}

/* Image */
img {
    max-width: 40%;
    height: auto;
    display: block;
    margin: 0 auto;
    border-radius: 18px;
    box-shadow: 0px 8px 18px rgba(0, 0, 0, 0.25);
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="header-container">
    <p class='main-title'>🍽️ Sistem Klasifikasi Citra Makanan Indonesia</p>
    <p class='sub-title'>Hybrid Transfer Learning ResNet50 dan Support Vector Machine (SVM)</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/1046/1046784.png",
    width=100
)

st.sidebar.title("Tentang Penelitian")
st.sidebar.write("""
### Judul Project
**Penerapan Hybrid Transfer Learning ResNet50 dan Support Vector Machine (SVM) 
untuk Klasifikasi Citra Makanan Indonesia dengan Penyajian Informasi Nilai Gizi Indonesia Berbasis Web Streamlit**
""")

st.sidebar.info("""
**Cara Menggunakan Aplikasi:**
1. Upload gambar makanan.
2. Sistem akan melakukan klasifikasi.
3. Hasil prediksi akan ditampilkan.
4. Informasi nilai gizi akan muncul secara otomatis.
""")
st.sidebar.success("Status Model: Siap Digunakan")

# ============================================================
# LOAD MODEL & DATABASE (CACHED)
# ============================================================
@st.cache_resource
def load_feature_extractor():
    model = timm.create_model(
        "hf_hub:anonauthors/food101-resnet50",
        pretrained=True,
        num_classes=0
    )
    for param in model.parameters():
        param.requires_grad = False
    model.eval()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    data_config = resolve_model_data_config(model)
    transform = create_transform(**data_config)
    return model, transform, device

@st.cache_resource
def load_svm():
    return joblib.load(os.path.join(MODEL_DIR, "svm_model.pkl"))

@st.cache_resource
def load_class_indices():
    return joblib.load(os.path.join(MODEL_DIR, "class_indices.pkl"))

@st.cache_resource
def load_scaler():
    return joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))

@st.cache_data
def load_database_gizi():
    csv_path = os.path.join(DATASET_DIR, "data_gizi_makanan_indonesia.csv")
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    df["Nama Makanan"] = df["Nama Makanan"].astype(str).str.strip()
    return df

# Load All Artifacts
feature_extractor, transform, device = load_feature_extractor()
scaler = load_scaler()
svm = load_svm()
class_indices = load_class_indices()
df_gizi = load_database_gizi()

idx_to_class = {v: k for k, v in class_indices.items()}

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def preprocess_image(image):
    return transform(image).unsqueeze(0).to(device)

def extract_feature(image):
    with torch.no_grad():
        feature = feature_extractor(image)
    return feature.cpu().numpy()

def get_nilai_gizi(nama_makanan):
    hasil = df_gizi[df_gizi["Nama Makanan"].str.lower() == nama_makanan.lower()]
    if hasil.empty:
        return None
    return hasil.iloc[0]

# ============================================================
# LAYOUT UTAMA (UPLOAD & PREVIEW BERSANDINGAN)
# ============================================================
col_upload, col_preview = st.columns([1, 1])

with col_upload:
    st.subheader("📤 Upload Gambar")
    uploaded_file = st.file_uploader(
        "Pilih gambar makanan",
        type=["jpg", "jpeg", "png"]
    )

with col_preview:
    st.subheader("🖼️ Preview Gambar")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(
            image,
            caption="Gambar yang di-upload",
            use_container_width=True
        )
    else:
        st.info("Silakan upload gambar makanan di sebelah kiri.")

# ============================================================
# PROSES PREDIKSI & HASIL
# ============================================================
if uploaded_file is not None:
    with st.spinner("Sedang melakukan klasifikasi..."):
        img = preprocess_image(image)
        feature = extract_feature(img)
        feature = scaler.transform(feature)
        pred = svm.predict(feature)
        confidence = svm.predict_proba(feature)
        
        kelas = idx_to_class[pred[0]].replace("_", " ")
        score = np.max(confidence)

    st.success("Prediksi selesai.")
    st.divider()

    # --- HASIL KLASIFIKASI ---
    st.header("🎯 Hasil Klasifikasi")
    col_hasil1, col_hasil2 = st.columns(2)
    
    with col_hasil1:
        st.metric(label="🍽️ Jenis Makanan", value=kelas)
    with col_hasil2:
        st.metric(label="🎯 Confidence", value=f"{score*100:.2f}%")

    st.progress(float(score))
    st.divider()

    # --- INFORMASI NILAI GIZI ---
    st.header("📊 Informasi Nilai Gizi")
    st.caption("Berdasarkan 100 gram makanan")
    
    gizi = get_nilai_gizi(kelas)

    if gizi is not None:
        gizi_col1, gizi_col2, gizi_col3, gizi_col4 = st.columns(4)

        with gizi_col1:
            st.metric("🔥 Energi", f"{gizi['Energi (kkal/100 g)']} kkal")
        with gizi_col2:
            st.metric("🥩 Protein", f"{gizi['Protein (g/100 g)']} g")
        with gizi_col3:
            st.metric("🧈 Lemak", f"{gizi['Lemak (g/100 g)']} g")
        with gizi_col4:
            st.metric("🍚 Karbohidrat", f"{gizi['Karbohidrat (g/100 g)']} g")

        st.info(f"📚 Sumber Data: {gizi['Sumber Data']}")

        # --- DOWNLOAD HASIL ---
        hasil_text = f"""
==========================================
HASIL KLASIFIKASI MAKANAN INDONESIA
==========================================

Nama Makanan : {kelas}
Confidence   : {score*100:.2f} %

Informasi Nilai Gizi (100 gram):
- Energi     : {gizi['Energi (kkal/100 g)']} kkal
- Protein    : {gizi['Protein (g/100 g)']} g
- Lemak      : {gizi['Lemak (g/100 g)']} g
- Karbohidrat : {gizi['Karbohidrat (g/100 g)']} g

Sumber Data  : {gizi['Sumber Data']}
"""
        st.download_button(
            label="📥 Download Hasil Prediksi",
            data=hasil_text,
            file_name="hasil_prediksi.txt",
            mime="text/plain"
        )
    else:
        st.warning("Informasi nilai gizi belum tersedia di database.")

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown("""
<div style="text-align:center; color:#808080; font-size:14px;">
<b>Sistem Klasifikasi Citra Makanan Indonesia</b><br>
Hybrid Transfer Learning ResNet50 + Support Vector Machine (SVM)<br>
Penyajian Informasi Nilai Gizi Indonesia<br><br>
Developed by <b>Yogi Irawan</b><br>
<a href="https://github.com/ogikkoding" target="_blank" style="color:#26A69A;">
github.com/ogikkoding
</a>
</div>
""", unsafe_allow_html=True)
