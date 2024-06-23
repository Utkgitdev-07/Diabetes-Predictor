# Diabetes Prediction Project

This project is a Flask web application for predicting diabetes using various machine learning techniques. The best-performing model, a decision tree, has been implemented for training our diabetes predictor.

## Project Structure

- `dataset/` - Contains the dataset files.
- `model/` - Contains the trained model `.pkl` files.
- `notebook/` - Contains Jupyter notebooks used for model training and evaluation.
- `templates/` - Contains HTML templates for the Flask application.
- `app.py` - The main Flask application file.
- `data.json` - Contains additional data used by the application.

## Setup Instructions

### Step 1: Create a virtual environment

Before running the application, you need to create a virtual environment for Flask.

```bash
python -m venv venv


### Step 2: Activate the virtual environment

On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate


### Step 3: Install the required packages
Install the dependencies listed in the requirements.txt file.
pip install -r requirements.txt


### Step 4: Run the Flask application
To start the Flask application, run:
python app.py


### Step 5: Access the Flask application
Open a new tab in your browser and paste the following URL:
https://{your_url} for home page and https://{your_url}/predictdata for prediction
Replace {your_url} with your specific URL.


### Project Details

Notebooks

Decision Tree - Contains the decision tree model.
Naive Bayes - Contains the naive bayes model.
SVM - Contains the support vector machine model.
Logistic Regression - Contains the logistic regression model.


Model Evaluation
Among all the techniques, we found that the decision tree performed the best for our diabetes predictor model.

Author
[Utkarsh Yadav]

License
This project is licensed under the MIT License.

Copy this entire block into your README file to have the complete, correctly formatted content.
