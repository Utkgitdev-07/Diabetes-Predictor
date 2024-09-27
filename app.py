from flask import Flask, request, render_template
import pickle
import pandas as pd

application = Flask(__name__)
app = application

# Load the StandardScaler and model from pickle files
scaler = pickle.load(open(r"Model\standardScalar.pkl", "rb"))
model = pickle.load(open(r"Model\modelForPrediction.pkl", "rb"))

# Define the feature names used during model training
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for single data point prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""

    if request.method == 'POST':
        # Get form inputs
        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        # Create a DataFrame for the input data with correct feature names
        input_data = pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]],
                                  columns=feature_names)

        # Apply the scaler to the input data
        scaled_data = scaler.transform(input_data)

        # Make a prediction using the trained model
        predict = model.predict(scaled_data)

        # Interpret the result
        if predict[0] == 1:
            result = 'Diabetic'
        else:
            result = 'Non-Diabetic'

        # Render the result in the template
        return render_template('single_prediction.html', result=result)

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
