# 🩺 Diabetes Prediction Web App

This is a Flask-based web application that uses a machine learning model to predict whether a person is likely to have diabetes based on input health parameters. The model is trained using the popular Pima Indians Diabetes Dataset.

---

## 🚀 Features

- User-friendly web interface built with HTML and Bootstrap
- Accepts health parameters like glucose level, blood pressure, BMI, etc.
- Predicts diabetes likelihood using a trained machine learning model (`model.pkl`)
- Built with Flask, scikit-learn, pandas, and numpy

---

## 🧰 Tech Stack

- Python
- Flask
- scikit-learn
- Pandas
- NumPy
- HTML/CSS/Bootstrap

---

## 📁 Project Structure

db-predict-app/
├── static/
├── templates/
│ └── index.html
├── model.pkl
├── app.py
├── requirements.txt
└── README.md  

## 💻 How to Run Locally
1. Clone the Repository
2. Create and Activate Virtual Environment
  # Windows
     python -m venv venv
     venv\Scripts\activate

  # Linux/Mac
     python3 -m venv venv
     source venv/bin/activate

3. Install Requirements
   pip install -r requirements.txt
   
4. Run the App
   python app.py


