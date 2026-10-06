# 🍽️ Indonesian Food Image Classification Using Hybrid Transfer Learning (ResNet50) and Support Vector Machine (SVM)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-SVM-f7931e)
![License](https://img.shields.io/badge/License-MIT-green)

> A web-based Indonesian food image classification system developed using a **Hybrid Deep Learning and Machine Learning** approach. The application employs **ResNet50** as a deep feature extractor and **Support Vector Machine (SVM)** as the classifier, while automatically presenting nutritional information based on prediction results.

---

# 📖 Overview

This project presents an intelligent web application for classifying Indonesian food images using a hybrid architecture that combines **Deep Learning** and **Machine Learning**.

Instead of performing end-to-end classification, the pretrained **ResNet50** network is utilized solely as a **feature extractor** to generate high-level visual representations of food images. These extracted features are subsequently classified using a **Support Vector Machine (SVM)**, resulting in high classification performance.

To provide additional value for users, the application automatically retrieves nutritional information from an Indonesian food nutrition database, including:

- 🔥 Calories
- 🥩 Protein
- 🧈 Fat
- 🍚 Carbohydrates

The system is deployed as an interactive web application using **Streamlit**, allowing users to classify food images quickly and conveniently.

---

# ✨ Features

- 📤 Upload Indonesian food images
- 🤖 Automatic food classification using ResNet50 + SVM
- 📊 Confidence score visualization
- 🥗 Automatic nutritional information retrieval
- 🔥 Calories estimation
- 🥩 Protein information
- 🧈 Fat information
- 🍚 Carbohydrate information
- 💾 Download prediction summary
- 🌐 Interactive Streamlit-based web interface

---

# 🖼️ Application Preview

## 🏠 Home Page

The landing page displayed before users perform image classification.

![Home](IMAGES/home.png)

---

## 🔍 Prediction Result

Displays the predicted food category, confidence score, and nutritional information.

![Prediction](IMAGES/prediksi.png)

---

## 🎥 Application Workflow

Illustration of the complete classification workflow.

![Demo](IMAGES/Gizi_makanan.gif)

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

The classification workflow consists of the following stages:

1. Upload an Indonesian food image.
2. Perform image preprocessing.
3. Extract deep visual features using **ResNet50**.
4. Normalize the feature vector using **StandardScaler**.
5. Classify the extracted features using **Support Vector Machine (SVM)**.
6. Retrieve nutritional information from the food nutrition database.
7. Display prediction results together with nutritional facts on the Streamlit interface.

---

# 🏗️ Project Structure

```text
project/
│
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
│   ├── dataset_makanan.png
│   ├── pipeline.png
│   ├── architecture.png
│   ├── output.png
│   └── Gizi_makanan.gif
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

The project was developed using the following technologies:

- 🐍 Python
- 🌐 Streamlit
- 🔥 PyTorch
- 🖼️ TIMM (PyTorch Image Models)
- 🧠 ResNet50
- 🤖 Scikit-learn
- 📊 Support Vector Machine (SVM)
- 🐼 Pandas
- 🔢 NumPy
- 🖼️ Pillow

---

# 📊 Dataset

The dataset consists of Indonesian food images collected from publicly available sources for training and evaluating the classification model.

## Dataset Sources

### Indonesian Food Image Dataset

https://www.kaggle.com/datasets/putriayusalsabila/datasetpenelitian

### Nutritional Database

https://www.fatsecret.co.id/

---

## Nutritional Attributes

The nutritional database provides:

- 🔥 Calories
- 🥩 Protein
- 🧈 Fat
- 🍚 Carbohydrates

---

## 🖼️ Dataset Samples

![Dataset](IMAGES/dataset_makanan.png)

---

# 📈 Prediction Output

After classification, the application displays:

- 🍽️ Predicted Food Category
- 📊 Confidence Score
- 🔥 Calories
- 🥩 Protein
- 🧈 Fat
- 🍚 Carbohydrates

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/username/project.git
```

---

## 2. Navigate to the Project Folder

```bash
cd project
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

Once the server starts successfully, Streamlit will automatically open the application in your web browser.

---

# 💻 Development Environment

This project was developed using:

- Google Colab
- Visual Studio Code
- Streamlit
- Google Drive

---

# 👨‍💻 Developer

## Yogi Irawan

**Undergraduate Student of Informatics Engineering**

### Research Interests

- Artificial Intelligence
- Computer Vision
- Deep Learning
- Machine Learning

### Contact

📧 Email

yogiirawan490@gmail.com

💼 LinkedIn

https://www.linkedin.com/in/yogi-irawan-ab146a387

🐙 GitHub

https://github.com/username

---

# 🤝 Contributing

Contributions are welcome!

If you discover bugs, have ideas for improvements, or would like to add new features, please feel free to:

- Open an Issue
- Submit a Pull Request

---

# ⭐ Support

If you find this project useful, please consider giving this repository a ⭐.

Your support helps motivate future improvements and development.

---

# 📄 License

This project is distributed under the **MIT License**.

Copyright © 2026 **Yogi Irawan**
