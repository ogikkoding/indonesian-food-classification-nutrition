# 🍽️ Indonesian Food Image Classification Using Hybrid Transfer Learning (ResNet50) and Support Vector Machine (SVM)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-SVM-f7931e)
![License](https://img.shields.io/badge/License-MIT-green)

> A web-based Indonesian food image classification system built with **Streamlit** that utilizes a **Hybrid Deep Learning and Machine Learning** approach, leveraging **ResNet50** as a feature extractor and **Support Vector Machine (SVM)** as the classifier. The application automatically displays nutritional information based on prediction results.

---

# 📖 Overview

This project aims to develop a web-based image classification system for Indonesian food by combining **Deep Learning** and **Machine Learning** techniques.

The **ResNet50** model serves as a **feature extractor** to extract deep visual representations from food images. Subsequently, these extracted features are classified using the **Support Vector Machine (SVM)** algorithm, achieving high prediction accuracy across food categories.

In addition to image classification, the application automatically retrieves and displays nutritional data from an Indonesian food nutrition database. Provided nutritional details include calories, protein, fat, and carbohydrates, helping users understand the nutritional breakdown of the recognized food item.

---

# 🖼️ Application Interface

## Home Page

> The landing interface of the application prior to running the classification workflow.

![Home](IMAGES/home.png)

---

## Prediction Results & Nutritional Info

> Displays the classification output along with the calculated confidence score.

![Prediction](IMAGES/prediksi.png)

---

### 🎥 Live Demo / Workflow

> Interactive classification workflow showing the process from image upload to nutritional evaluation.

![Demo Application](IMAGES/Gizi_makanan.gif)

---

# ✨ Key Features

- 📤 Upload Indonesian food images
- 🤖 Automatic classification powered by ResNet50 + Support Vector Machine
- 📊 Confidence score display for predictions
- 🥗 Automated retrieval of nutritional facts
- 🔥 Displays Calories, Protein, Fat, and Carbohydrates
- 💾 Download prediction summary
- 🌐 Interactive web UI built with Streamlit

---

# 🧠 Methodology

## Deep Learning

- Transfer Learning
- ResNet50
- Feature Extraction

## Machine Learning

- StandardScaler
- Support Vector Machine (SVM)

---

# ⚙️ System Pipeline

The execution flow of the system consists of the following steps:

1. The user uploads an image of Indonesian food via the web interface.
2. The image undergoes standard preprocessing steps.
3. The **ResNet50** model extracts high-level visual features from the preprocessed image.
4. The generated feature vector is scaled using **StandardScaler**.
5. The **Support Vector Machine (SVM)** classifies the feature vector into a food category.
6. The system queries the nutritional database using the predicted class label.
7. Prediction results and nutritional details are rendered to the user on the Streamlit interface.

```

# 📂 Project Structure

project/
├── STREAMLIT NUTRITION/
│ ├── app.py
│ └── run.bat
│
├── DATASET/
│ └── indonesian_food_nutrition_database.xlsx
│
├── MODELS/
│ ├── svm_model.pkl
│ ├── scaler.pkl
│ └── class_indices.pkl
│
├── IMAGES/
│ ├── home.png
│ ├── prediksi.png
│ ├── gizi.png
│ ├── pipeline.png
│ ├── architecture.png
│ ├── dataset.png
│ └── output.png
│
├── requirements.txt
└── README.md

---

# 🛠️ Tech Stack & Tools

This project was built using the following libraries and tools:

- 🐍 Python
- 🌐 Streamlit
- 🔥 PyTorch
- 🧠 TIMM (PyTorch Image Models)
- 🖼️ ResNet50
- 🤖 Scikit-learn
- 📊 Support Vector Machine (SVM)
- 🐼 Pandas
- 🔢 NumPy
- 🖼️ Pillow

---

# 📊 Dataset

The dataset consists of various Indonesian food images collected from multiple sources to train and evaluate the classification model.

## Dataset Sources

- **Indonesian Food Image Dataset (Kaggle)**
  https://www.kaggle.com/datasets/putriayusalsabila/datasetpenelitian

- **Nutritional Reference Data**
  https://www.fatsecret.co.id/

Nutritional information tracked includes:

- 🔥 Calories (Energy)
- 🥩 Protein
- 🧈 Fat
- 🍚 Carbohydrates

---

## 🖼️ Dataset Samples

![Dataset](IMAGES/dataset_makanan.png)

---

# 📋 System Output

Upon completing classification, the app provides:

- 🍽️ Predicted Food Name
- 📊 Confidence Score
- 🔥 Calories
- 🥩 Protein
- 🧈 Fat
- 🍚 Carbohydrates

---

# 🚀 Getting Started

## 1. Clone the Repository

git clone https://github.com/username/project.git

---

## 2. Navigate to the Project Directory

cd project

---

## 3. Install Dependencies

pip install -r requirements.txt

---

## 4. Run the Streamlit Application

streamlit run app.py

The browser should automatically open the interface once the server is ready.

---

# 💻 Development Environment

Developed using:

- Google Colab
- Visual Studio Code
- Google Drive
- Streamlit

---

# 👨‍💻 Developer

## Yogi Irawan

🎓 Informatics Engineering Student

🤖 Focus Areas:
Artificial Intelligence, Computer Vision, Deep Learning, and Machine Learning.

📧 Email
yogiirawan490@gmail.com

💼 LinkedIn
https://www.linkedin.com/in/yogi-irawan-ab146a387

🐙 GitHub
https://github.com/username

---

# 🤝 Contributing

Contributions are welcome!

If you encounter bugs, have suggestions, or wish to contribute new features, feel free to submit an Issue or open a Pull Request.

---

# ⭐ Support

If you find this project useful, please consider giving this repository a ⭐ to support its development!

---

# 📄 License

Distributed under the MIT License.
Copyright (c) 2026 Yogi Irawan
```
