# ============================================================
# SISTEM KLASIFIKASI CITRA MAKANAN INDONESIA
# Hybrid Transfer Learning ResNet50 + Support Vector Machine
# ============================================================
import streamlit as st
from PIL import Image

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Klasifikasi Makanan Indonesia",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS CUSTOM MODERN
# ============================================================

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#0F172A,#111827,#000000);
}

/* Main Title */
.main-title{
    text-align:center;
    color:#00897B;
    font-size:42px;
    font-weight:700;
    margin-bottom:5px;
    letter-spacing:1px;
}

/* Subtitle */
.sub-title{
    text-align:center;
    color:#616161;
    font-size:19px;
    margin-bottom:30px;
}

/* Card */
.box{
    background:white;
    padding:25px;
    border-radius:20px;
    border:1px solid #E0E0E0;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
    transition:0.3s;
}

.box:hover{
    transform:translateY(-3px);
    box-shadow:0px 12px 25px rgba(0,0,0,0.12);
}

/* Result Card */
.result-box{
    background:linear-gradient(135deg,#E8F5E9,#F1F8E9);
    padding:25px;
    border-radius:20px;
    border-left:8px solid #43A047;
    box-shadow:0px 10px 20px rgba(67,160,71,.15);
}

/* Metric Box */
.metric-box{
    background:white;
    padding:18px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 5px 12px rgba(0,0,0,.08);
    transition:.25s;
}

.metric-box:hover{
    transform:scale(1.03);
}

/* Footer */
.footer{
    text-align:center;
    color:#757575;
    font-size:14px;
    margin-top:40px;
}

/* Buttons */
.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#26A69A,#00897B);
    color:white;
    border:none;
    border-radius:12px;
    font-size:17px;
    font-weight:bold;
    padding:12px;
    transition:0.3s;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#00897B,#00695C);
    transform:scale(1.02);
}

/* File Uploader */
[data-testid="stFileUploader"]{
    border:2px dashed #26A69A;
    border-radius:15px;
    padding:20px;
    background:#FCFFFE;
}

/* Success */
.stSuccess{
    border-radius:12px;
}

/* Spinner */
.stSpinner>div{
    color:#00897B;
}

/* Image */
img{
    border-radius:18px;
    box-shadow:0px 8px 18px rgba(0,0,0,.12);
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    "<p class='main-title'>🍽️ Sistem Klasifikasi Citra Makanan Indonesia</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Hybrid Transfer Learning ResNet50 dan Support Vector Machine (SVM)</p>",
    unsafe_allow_html=True
)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/1046/1046784.png",
    width=120
)

st.sidebar.title("Tentang Penelitian")
st.sidebar.write("""

### Judul project

**Penerapan Hybrid Transfer Learning ResNet50 dan Support Vector Machine (SVM)
untuk Klasifikasi Citra Makanan Indonesia
dengan Penyajian Informasi Nilai Gizi Indonesia
Berbasis Web Streamlit**

""")

st.sidebar.info("""
Cara menggunakan aplikasi:

1. Upload gambar makanan.
2. Sistem akan melakukan klasifikasi.
3. Hasil prediksi akan ditampilkan.
4. Informasi nilai gizi akan muncul secara otomatis.
""")
st.sidebar.success("Status Model : Siap Digunakan")

# ============================================================
# LAYOUT
# ============================================================
col1, col2 = st.columns([1,1])

# ============================================================
# KOLOM KIRI
# ============================================================
with col1:

    st.subheader("📤 Upload Gambar")
    uploaded_file = st.file_uploader(
        "Pilih gambar makanan",
        type=["jpg","jpeg","png"]
    )

    st.markdown("---")

    st.subheader("🖼️ Preview Gambar")

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Gambar yang diupload",
            use_container_width=True
        )

    else:

        st.info("Silakan upload gambar makanan.")

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown("""
<div class='footer'>
Skripsi Informatika • 2026
Hybrid Transfer Learning ResNet50 + Support Vector Machine (SVM)
Dikembangkan menggunakan Streamlit

</div>
""", unsafe_allow_html=True)

# ============================================================
# LOAD MODEL RESNET50 + SVM
# ============================================================
import numpy as np
import joblib
import torch
import timm
from timm.data import resolve_model_data_config
from timm.data.transforms_factory import create_transform

# ============================================================
# LOAD RESNET50
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

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    model.to(device)

    data_config = resolve_model_data_config(model)
    transform = create_transform(**data_config)

    return model, transform, device

# ============================================================
# LOAD SVM
# ============================================================

@st.cache_resource
def load_svm():
    svm = joblib.load(
        r"D:\PROJECT CODING\PROGRAM\AI\PROJECT AI\ESTIMASI NILAI GIZI\MODELS\svm_model.pkl"
    )
    return svm

# ============================================================
# LOAD CLASS INDICES
# ============================================================

@st.cache_resource
def load_class_indices():
    class_indices = joblib.load(
        r"D:\PROJECT CODING\PROGRAM\AI\PROJECT AI\ESTIMASI NILAI GIZI\MODELS\class_indices.pkl"
    )
    return class_indices
# ============================================================
# LOAD SCALER
# ============================================================

@st.cache_resource
def load_scaler():
    scaler = joblib.load(
        r"D:\PROJECT CODING\PROGRAM\AI\PROJECT AI\ESTIMASI NILAI GIZI\MODELS\scaler.pkl"
    )
    return scaler

# ============================================================
# LOAD MODEL
# ============================================================

feature_extractor, transform, device = load_feature_extractor()
scaler = load_scaler()
svm = load_svm()
class_indices = load_class_indices()
# Mengubah dictionary dari nama->index menjadi index->nama
idx_to_class = {v: k for k, v in class_indices.items()}

# ============================================================
# PREPROCESSING
# ============================================================

def preprocess_image(image):
    return transform(image).unsqueeze(0).to(device)

# ============================================================
# FEATURE EXTRACTION
# ============================================================

def extract_feature(image):
    with torch.no_grad():
        feature = feature_extractor(image)
    return feature.cpu().numpy()

# ============================================================
# PREDIKSI
# ============================================================

if uploaded_file is not None:
    with st.spinner("Sedang melakukan klasifikasi..."):
        # Preprocessing gambar
        img = preprocess_image(image)
        # Ekstraksi fitur
        feature = extract_feature(img)
        # Normalisasi feature
        feature = scaler.transform(feature)
        # Prediksi
        pred = svm.predict(feature)
        # Confidence
        confidence = svm.predict_proba(feature)
        # Nama kelas
        kelas = idx_to_class[pred[0]].replace("_", " ")
        # Nilai confidence tertinggi
        score = np.max(confidence)
    st.success("Prediksi selesai.")
 
# ============================================================
# DATABASE INFORMASI NILAI GIZI
# ============================================================
import pandas as pd

# ============================================================
# LOAD DATABASE GIZI
# ============================================================

@st.cache_data
def load_database_gizi():
    """
    Membaca database informasi nilai gizi
    """
    df = pd.read_csv("data_gizi_makanan_indonesia.csv")
    # Membersihkan nama kolom
    df.columns = df.columns.str.strip()

    # Membersihkan nama makanan
    df["Nama Makanan"] = (
        df["Nama Makanan"]
        .astype(str)
        .str.strip()
    )

    return df


# ============================================================
# LOAD DATABASE
# ============================================================

df_gizi = load_database_gizi()

# ============================================================
# FUNGSI MENCARI DATA GIZI
# ============================================================

def get_nilai_gizi(nama_makanan):

    hasil = df_gizi[
        df_gizi["Nama Makanan"].str.lower()
        ==
        nama_makanan.lower()
    ]

    if hasil.empty:
        return None

    return hasil.iloc[0]


# ============================================================
# AMBIL DATA BERDASARKAN HASIL PREDIKSI
# ============================================================

gizi = None
if uploaded_file is not None:
    gizi = get_nilai_gizi(kelas)

# ============================================================
# PART 4
# MENAMPILKAN HASIL PREDIKSI DAN INFORMASI GIZI
# ============================================================

if uploaded_file is not None:
    st.divider()
    st.header("🎯 Hasil Klasifikasi")
    col_hasil1, col_hasil2 = st.columns(2)
    with col_hasil1:
        st.metric(
            label="🍽️ Jenis Makanan",
            value=kelas
        )
    with col_hasil2:
        st.metric(
            label="🎯 Confidence",
            value=f"{score*100:.2f}%"
        )

    st.progress(float(score))
    st.divider()
    st.header("📊 Informasi Nilai Gizi")
    st.caption("Berdasarkan 100 gram makanan")
    if gizi is not None:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🔥 Energi",
                f"{gizi['Energi (kkal/100 g)']} kkal"
            )

        with col2:
            st.metric(
                "🥩 Protein",
                f"{gizi['Protein (g/100 g)']} g"
            )

        with col3:
            st.metric(
                "🧈 Lemak",
                f"{gizi['Lemak (g/100 g)']} g"
            )

        with col4:
            st.metric(
                "🍚 Karbohidrat",
                f"{gizi['Karbohidrat (g/100 g)']} g"
            )

        st.success("✅ Informasi gizi berhasil dimuat.")

        st.info(
            f"📚 Sumber Data : {gizi['Sumber Data']}"
        )

    else:

        st.warning(
            "Informasi nilai gizi belum tersedia."
        )

    # ========================================================
    # DOWNLOAD HASIL
    # ========================================================

    if gizi is not None:
        hasil = f"""

==========================================
HASIL KLASIFIKASI MAKANAN INDONESIA
==========================================

Nama Makanan : {kelas}
Confidence : {score*100:.2f} %
Informasi Nilai Gizi (100 gram)

Energi       : {gizi['Energi (kkal/100 g)']} kkal
Protein      : {gizi['Protein (g/100 g)']} g
Lemak        : {gizi['Lemak (g/100 g)']} g
Karbohidrat  : {gizi['Karbohidrat (g/100 g)']} g

Sumber Data :
{gizi['Sumber Data']}
"""
        st.download_button(
            label="📥 Download Hasil Prediksi",
            data=hasil,
            file_name="hasil_prediksi.txt",
            mime="text/plain"
        )

# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown(
"""
<div style="text-align:center; color:#808080; font-size:14px;">
<b>Sistem Klasifikasi Citra Makanan Indonesia</b><br>
Hybrid Transfer Learning ResNet50 + Support Vector Machine (SVM)<br>
Penyajian Informasi Nilai Gizi Indonesia<br><br>
Developed by <b>Yogi Irawan</b><br>
<a href="https://github.com/ogikkoding" target="_blank">
github.com/ogikkoding
</a>

</div>
""",
unsafe_allow_html=True
)