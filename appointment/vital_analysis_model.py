import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset path (adjust the dataset path if needed)
DATASET_FILE = os.path.join('appointment', 'human_vital_signs_dataset_2024.csv')

# Check if the dataset file exists
if not os.path.isfile(DATASET_FILE):
    raise FileNotFoundError(f"File '{DATASET_FILE}' does not exist in the directory.")

def load_dataset():
    """Load the dataset from the CSV file."""
    df = pd.read_csv(DATASET_FILE)
    df.columns = df.columns.str.strip()  # Trim whitespace from column names
    return df

def train_ml_model():
    """Train the Logistic Regression model on the dataset."""
    # Load the dataset
    df = load_dataset()

    required_columns = [
        'Heart Rate', 'Respiratory Rate', 'Body Temperature', 
        'Oxygen Saturation', 'Systolic Blood Pressure', 
        'Diastolic Blood Pressure', 'Risk Category'
    ]

    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not found in dataset. Available columns: {df.columns.tolist()}")

    # Features and target variable
    X = df[required_columns[:-1]]
    y = df['Risk Category']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Logistic Regression model
    model = LogisticRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy:.2f}')

    # Save the trained model to a file
    joblib.dump(model, 'vital_signs_model.pkl')
    return model

def load_trained_model():
    """Load the trained model from the file."""
    return joblib.load('vital_signs_model.pkl')

def predict_risk_with_ml(model, heart_rate, respiratory_rate, body_temperature, 
                          oxygen_saturation, systolic_blood_pressure, diastolic_blood_pressure):
    """Make predictions based on user input."""
    input_data = [[heart_rate, respiratory_rate, body_temperature, 
                   oxygen_saturation, systolic_blood_pressure, diastolic_blood_pressure]]

    # Predict the risk category
    prediction = model.predict(input_data)

    return prediction[0]  # Return the predicted risk category

def generate_issues_report(risk_category):
    """Generate a report based on the predicted risk category."""
    issues = {
        "Low Risk": "No immediate concerns detected. Maintain a healthy lifestyle.",
        "High Risk": "Possible health issues detected. Consider consulting a healthcare provider. Conditions may include hypertension, respiratory distress, or other cardiovascular issues."
    }

    report = f"Predicted Risk Category: {risk_category}\n"
    report += "Health Issues:\n"
    report += issues[risk_category] + "\n"
    
    # Save the report to a file
    with open('patient_issues_report.txt', 'w') as file:
        file.write(report)
    
    print("Issues report generated as 'patient_issues_report.txt'.")
    return report
