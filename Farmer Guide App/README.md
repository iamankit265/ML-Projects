# 🌾 Farmer Guide App

## Project Description

Farmer Guide App is a Machine Learning-based web application that helps farmers make better agricultural decisions by providing intelligent recommendations.

The application offers two core functionalities:

- **Crop Recommendation** – Predicts the most suitable crop based on soil and environmental conditions.
- **Fertilizer Recommendation** – Suggests the appropriate fertilizer depending on soil nutrients and crop requirements.

The project combines Machine Learning with a Flask backend and a simple web interface to provide fast and accurate recommendations.

---

# Features

Crop Recommendation using Machine Learning

Fertilizer Recommendation using Machine Learning

User-friendly web interface

Fast prediction using trained ML models

Input validation for user data

Responsive frontend

---

# Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Pickle

### Development Tools
- Jupyter Notebook
- VS Code
- Google Colab
- Git
- GitHub

---

# Project Structure

```
Farmer-Guide-App/
│
├── Data Set/
│   ├── Crop_recommendation.csv
│   └── fertiizer_recommendation_dataset.csv
│
├── model/
│   ├── crop_encoder.pkl
│   ├── crop_label_encoder.pkl
│   ├── crop_model.pkl
│   ├── crop_scaler.pkl
│   ├── fertilizer_model.pkl
│   ├── fertilizer_crop_encoder.pkl
│   ├── fertilizer_encoder.pkl
│   ├── fertilizer_scaler.pkl
│   ├── fertilizer_soil_encoder.pkl
│   ├── fertilizer_scaler.pkl
│   └── soil_encoder.pkl
│
├── Notebooks/
│   ├── Train_Crop.ipynb
│   └── Train_Fertilizer.ipynb
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── crop.html
│   ├── fertilizer.html
│   ├── fertilizer_predict.html
│   └── crop_predict.html
│
├── app.py
├── Requirement.txt
├── README.md

```

---

# ML Flow

### Crop Recommendation

1. Collect crop dataset.
2. Perform data preprocessing.
3. Train the Machine Learning model.
4. Save the trained model using Pickle.
5. Load the model in Flask.
6. User enters soil and environmental parameters.
7. Model predicts the most suitable crop.
8. Display the recommendation.

---

### Fertilizer Recommendation

1. Collect fertilizer dataset.
2. Clean and preprocess the data.
3. Train the Machine Learning model.
4. Save the trained model.
5. Load the model into the Flask application.
6. User provides crop and soil information.
7. Model predicts the appropriate fertilizer.
8. Display the fertilizer recommendation.

---

# Installation

### 1. Clone the repository

```bash
git clone https://github.com/iamankit265/ML-Projects/

```

### 2. Navigate to the project

```bash
cd Farmer-Guide-App
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r Requirement.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open your browser

```
http://127.0.0.1:5000
```

---

# Future Enhancement

- Weather-based crop recommendation
- Disease prediction using image processing
- Yield prediction
- Market price prediction
- Multi-language support
- GPS-based location services
- Farmer profile management
- Cloud deployment
- Mobile application support

---

# Author

**Ankit Kumar**

