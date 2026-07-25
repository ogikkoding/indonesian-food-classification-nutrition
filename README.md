# 🍽️ Indonesian Food Image Classification Using Hybrid Transfer Learning ResNet50 and Support Vector Machine (SVM)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-SVM-f7931e)
![License](https://img.shields.io/badge/License-MIT-green)

> A web based Indonesian food image classification system built with Streamlit using a hybrid approach that combines ResNet50 as a feature extractor and Support Vector Machine (SVM) as the classifier, with automatic nutritional information retrieval.

---

# 📖 Description

This project aims to develop an Indonesian food image classification system by combining **Deep Learning** and **Machine Learning** techniques.

The **ResNet50** model is utilized as a feature extractor to obtain visual features from food images. These extracted features are then classified using a **Support Vector Machine (SVM)**.

In addition to food classification, the application automatically displays nutritional information based on an Indonesian food nutrition database, allowing users to view the nutritional content of the predicted food.

---

# 🖼️ Streamlit Application Preview

### Home Page

> The application's main page before prediction.

![Home](images/home.png)

---

### Prediction Result and Nutritional Information

> Predicted food category along with its confidence score.

![Prediction](IMAGES/prediksi.png)

---

### 🎥 Live Demo / Workflow

> Interactive classification process from image upload to nutritional evaluation.

![Demo Application](IMAGES/demo.gif)

---

# ✨ Features

- 📤 Upload Indonesian food images
- 🤖 Automatic food classification using ResNet50 + SVM
- 📊 Display prediction confidence score
- 🥗 Show nutritional information
- 🔥 Display calories, protein, fat, and carbohydrates
- 💾 Download prediction results
- 🌐 User-friendly Streamlit web interface

---

# 🧠 Methods

## Deep Learning

- Transfer Learning
- ResNet50
- Feature Extraction

## Machine Learning

- StandardScaler
- Support Vector Machine (SVM)

---

# 🔄 System Pipeline

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
Food Classification
   │
   ▼
Nutrition Database Lookup
   │
   ▼
Nutritional Information
   │
   ▼
Streamlit Web Application
```

---

## 🖼️ Pipeline Diagram

![Pipeline](images/pipeline.png)

---

# 🏗️ System Architecture

```text
Food Image
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
Prediction
     │
     ▼
Nutrition Database
     │
     ▼
Nutritional Information
     │
     ▼
Streamlit Web Application
```

---

## 🖼️ Architecture Diagram

![Architecture](images/architecture.png)

---

# ⚙️ System Workflow

1. The user uploads a food image.
2. The system preprocesses the image.
3. ResNet50 extracts image features.
4. The extracted feature vector is normalized using StandardScaler.
5. Support Vector Machine performs the classification.
6. The system retrieves nutritional information based on the predicted food.
7. The nutritional information is displayed to the user.

---

# 📂 Project Structure

```text
project/

├── STREAMLIT NUTRITION/
│   ├── app.py
│   └── run.bat
│
├── DATASET/
│   └── indonesian_food_nutrition_database.xlsx
│
├── MODELS/
│   ├── svm_model.pkl
│   ├── scaler.pkl
│   └── class_indices.pkl
│
├── IMAGES/
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

# 🛠️ Technologies Used

- Python
- Streamlit
- PyTorch
- TIMM
- ResNet50
- Scikit-learn
- Support Vector Machine (SVM)
- Pandas
- NumPy
- Pillow

---

# 📊 Dataset

The dataset used in this project was collected from multiple sources to support Indonesian food image classification.

## Data Sources

- Indonesian Food Image Dataset (Kaggle):
  https://www.kaggle.com/datasets/putriayusalsabila/datasetpenelitian

- Food Nutrition Reference:
  https://www.fatsecret.co.id/

The nutritional information includes:

- Calories (Energy)
- Protein
- Fat
- Carbohydrates

---

## 🖼️ Sample Dataset

![Dataset](images/dataset.png)

---

# 📋 System Output

The application provides:

- Predicted Food Name
- Confidence Score
- Calories
- Protein
- Fat
- Carbohydrates

---

## 🖼️ Sample Output

![Output](images/output.png)

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/username/project.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 💻 Development Environment

- Google Colab
- Visual Studio Code
- Google Drive
- Streamlit

---

# 👨‍💻 Developer

**Yogi Irawan**

🎓 Bachelor's Student in Informatics

🤖 Research Interests: Artificial Intelligence & Computer Vision

📧 Email: yogiirawan490@gmail.com

💼 LinkedIn:
https://www.linkedin.com/in/yogi-irawan-ab146a387

🐙 GitHub:
https://github.com/username

---

# 📄 License

MIT License

Copyright (c) 2026 Yogi Irawan
