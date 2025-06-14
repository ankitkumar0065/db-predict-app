import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Session ke liye secret key chahiye

@app.route('/')
def home():
    return render_template('login.html')  # wo updated login HTML file

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('name')
    if username:
        session['username'] = username  # session me username save kar lo
        return redirect(url_for('instructions'))
    else:
        return "Please enter your name", 400

@app.route('/instructions')
def instructions():
    username = session.get('username')
    if not username:
        return redirect(url_for('home'))
    return render_template('instruction.html', username=username)

@app.route('/health_form')
def health_form():
    return render_template('health_form.html', name=session.get('username'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        data = [
            float(request.form['pregnancies']),
            float(request.form['glucose']),
            float(request.form['bloodpressure']),
            float(request.form['skinthickness']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['dpf']),
            float(request.form['age'])
        ]

        # Scale the input
        scaled_input = scaler.transform([data])

        # Make prediction
        result = model.predict(scaled_input)

        prediction = "You are Diabetic 😟" if result[0] == 1 else "You are Non-Diabetic 😊"
        

        return render_template('result.html', name=session.get('username'), prediction=prediction)

    except Exception as e:
        return f"Error in prediction: {str(e)}"
    

# Aage ke routes jese health info form, prediction etc.

if __name__ == '__main__':
    app.run(debug=True)
