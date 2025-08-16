from flask import Flask, render_template, request
import numpy as np
# from joblib import load  # Uncomment if you're loading a model

app = Flask(__name__)

# Load your model here
# model = load('model/autism_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            gender = request.form['gender']
            ethnicity = request.form['ethnicity']
            jaundice = request.form['jaundice']
            autism_family = request.form['autism_family']
            country = request.form['country']
            app_used = request.form['app_used']
            score = int(request.form['score'])
            age_desc = request.form['age_desc']
            relation = request.form['relation']

            # Normally you'd encode this and predict:
            # input_data = np.array([[age, gender_encoded, ..., relation_encoded]])
            # prediction = model.predict(input_data)
            # For now, we just fake it:
            prediction = "Positive" if score > 5 else "Negative"

            prediction_text = f"Prediction: {prediction} for Autism Risk"
        except:
            prediction_text = "Error in input. Please check your values."
    
    return render_template("index.html", prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)


