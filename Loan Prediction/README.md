# 💳 Loan Prediction

## Project Description

Loan Prediction is a Machine Learning-based web application that predicts whether a loan application is likely to be approved based on an applicant's personal, financial, and credit-related information.

The application uses a trained Machine Learning model to analyze various applicant attributes and instantly determine the loan approval status through a simple and user-friendly web interface.

---

# Features

Loan Approval Prediction using Machine Learning

User-friendly web interface

Real-time prediction

Input validation for user data

Fast prediction using trained ML model

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
Loan-Prediction/
│
├── Data Set/
│   └── credit_risk_dataset.csv
│
├── model/
│   ├── credit.pkl
│   ├── scaler.pkl
│   └── encoders.pkl
│
├── Notebooks/
│   └── Train_credit.ipynb
│
├── static/
│   ├── style.css
│   └── result.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── README.md
└── requirements.txt
```

---

# ML Flow

1. Collect the loan prediction dataset.
2. Perform data cleaning and preprocessing.
3. Encode categorical features.
4. Scale numerical features.
5. Train the Machine Learning model.
6. Save the trained model and preprocessing objects using Pickle.
7. Load the model into the Flask application.
8. User enters applicant details.
9. Model predicts whether the loan is likely to be Approved or Rejected.
10. Display the prediction on the result page.

---

# Installation

### 1. Clone the repository

```bash
git clone https://github.com/iamankit265/ML-Projects/Loan-Prediction.git
```

### 2. Navigate to the project

```bash
cd Loan-Prediction
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
pip install -r requirements.txt
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

# Input Features

- Person Age
- Person Income
- Home Ownership
- Employment Length
- Loan Intent
- Loan Grade
- Loan Amount
- Interest Rate
- Loan Percent Income
- Previous Loan Default
- Credit History Length

---

# Future Enhancement

- Probability score for loan approval
- Explainable AI (feature importance)
- Loan eligibility percentage
- Interactive dashboard with charts
- User authentication
- Database integration
- Cloud deployment
- REST API support
- Mobile-friendly interface

---

# Author

**Ankit Kumar**
