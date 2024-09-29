
# Gemini Health Care Chatbot

## Overview

The **Gemini Health Care Chatbot** is a Django-based healthcare assistant that helps patients analyze medical images and symptoms to identify potential health concerns. The chatbot provides detailed analysis, recommendations, and treatment options based on the provided input, whether it's a medical image or text description.

## Features

- **User Registration and Login**: Allows users to register, log in, and maintain a personalized profile.
- **Medical Image Analysis**: Patients can upload medical images, which the chatbot analyzes for abnormalities and potential health issues.
- **Symptom Analysis**: Patients can describe their symptoms, and the chatbot will suggest possible conditions and provide advice.
- **Doctor Recommendations**: Based on the user’s profile and symptoms, the bot suggests relevant doctors for appointment scheduling.
- **Gemini AI Integration**: Powered by Google Gemini's AI for generating responses to the uploaded images or user queries.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default in Django) or any Django-supported database
- **API Integration**: Google Gemini API for medical image and symptom analysis

## Prerequisites

Before setting up the project, make sure you have the following installed:

- Python 3.x
- Django 4.x or later
- Google Gemini API key

## Usage

1. **Register and Login**: Users must register and log in to access the chatbot.
2. **Profile Setup**: After login, users can access their profile to view personal information and their disease history.
3. **Upload Medical Images**: On the **Analyze Image** page, users can upload medical images or input symptoms for the chatbot to analyze.
4. **Receive Recommendations**: The chatbot provides detailed analysis, reports, recommendations, and potential treatments based on the input.

## Directory Structure

To be added. *(You can add your project's directory structure here.)*

## Models

### `UserProfile`

This model extends the default Django `User` model and stores additional information such as the user's disease history.

- **Fields**:
  - `user`: ForeignKey to `User`
  - `disease`: TextField

## API Integration

The chatbot uses Google Gemini's Generative AI API to process medical images and textual inputs. The integration is managed in `views.py` where the image or text is sent to the Gemini model, and a detailed response is generated.

---

# Vitals Monitoring and Prediction System

## Overview

The **Vitals Monitoring and Prediction System** is a Python-based solution that assesses an individual's health risk based on their key vital signs. By collecting inputs such as heart rate, respiratory rate, body temperature, oxygen saturation, and blood pressure, the system utilizes a trained Logistic Regression model to categorize the user's health status into either **Low Risk** or **High Risk**. Additionally, it generates comprehensive reports summarizing the findings, aiding in proactive healthcare management.

## Features

- **Vital Signs Collection**: Interactive input fields allow users to enter their heart rate, respiratory rate, body temperature, oxygen saturation, and blood pressure.
- **Risk Prediction**: The system uses a trained Logistic Regression model to evaluate the risk category based on the provided vital signs.
- **Automated Reporting**: A detailed text report (`patient_issues_report.txt`) is generated, summarizing the vital signs and the predicted risk category.
- **Model Training and Persistence**: The system can load a dataset, train a machine learning model, evaluate its accuracy, and save the trained model for future predictions.
- **Interactive Interface**: The project utilizes `ipywidgets` within a Jupyter Notebook for seamless and user-friendly data input and interaction.

## Technologies Used

- **Programming Language**: Python 3.x
- **Libraries and Frameworks**:
  - **Data Handling**: `pandas`
  - **Machine Learning**: `scikit-learn` (Logistic Regression), `joblib`
  - **Interactive UI**: `ipywidgets`, `IPython.display`
  - **File Operations**: `os`
- **Environment**: Jupyter Notebook for interactive execution and documentation

# Lung Cancer Prediction Model

## Overview

The **Lung Cancer Prediction Model** is a machine learning solution designed to predict the likelihood of lung cancer in individuals based on various health parameters. The model uses a dataset of lung cancer risk factors, such as age, smoking habits, and medical history, to classify individuals into different risk categories. This tool aids healthcare professionals and patients in proactive risk assessment, enabling timely medical interventions.

## Features

- **Risk Factor Input**: Users can input various health parameters like age, smoking status, alcohol consumption, and air pollution exposure.
- **Machine Learning Model**: The prediction is powered by a trained Vgg16,EfficientNetB0,InceptionV3, which classifies the input data into either **Low Risk** or **High Risk** categories.
- **Data Handling and Preprocessing**: The model processes raw input data, normalizes it, and makes it suitable for prediction.
- **Accuracy Evaluation**: The model can be evaluated for accuracy using common metrics like confusion matrix, precision, recall, and F1-score.
- **Automated Reporting**: The system generates a comprehensive report (`lung_cancer_risk_report.txt`) summarizing the risk factors and the predicted risk level.

## Technologies Used

- **Programming Language**: Python 3.x
- **Libraries and Frameworks**:
  - **Data Handling**: `pandas`
  - **Machine Learning**: `scikit-learn` (Logistic Regression, Decision Trees)
  - **Visualization**: `matplotlib`, `seaborn`
  - **Model Persistence**: `joblib` for saving the trained models
  - **Interactive Interface**: `ipywidgets` for collecting inputs in Jupyter Notebook

## Features

### 1. **Risk Prediction**
- Users can input relevant information, and the system predicts the likelihood of developing lung cancer using a trained model.

### 2. **Model Training**
- The system allows retraining using new datasets and provides functionality to save the trained models for future use.

### 3. **Visualization**
- Visualizes data distributions, risk categories, and the model's decision boundary using graphs and charts.

### 4. **Reporting**
- Generates a report that details the input parameters and the model's prediction, assisting users in understanding their lung cancer risk.

## Prerequisites

Make sure you have the following installed before setting up the project:

- Python 3.x
- Libraries:
  - `pandas`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `joblib`
  
## Model Inputs

The model takes the following inputs from users to predict lung cancer risk:

- **Age**: Integer
- **Smoking Status**: Boolean (True/False)
- **Alcohol Consumption**: Boolean (True/False)
- **Chronic Lung Disease**: Boolean (True/False)
- **Family History**: Boolean (True/False)
- **Air Pollution Exposure**: Boolean (True/False)

## Model Outputs

- **Risk Prediction**: Outputs the predicted risk of lung cancer as either **Low Risk** or **High Risk**.
- **Accuracy**: Displays the model's accuracy on the training and testing datasets.
- **Confusion Matrix**: Provides the confusion matrix for the model's predictions.
  
## Usage

1. **Input Data**: Users enter their health parameters.
2. **Run Prediction**: The system predicts lung cancer risk and displays the results.
3. **View Report**: The generated report is saved as `lung_cancer_risk_report.txt`, summarizing the inputs and predictions.






## Outputs

Below is an example of the system output:
for vital
![Vitals Monitoring Output](https://github.com/user-attachments/assets/ff2fbd25-dbc8-439f-9bce-d23b12cf4732)
![26389123-c644-4152-ab7d-105138747eb2](https://github.com/user-attachments/assets/9aca2fe8-2a6a-461f-9449-f5bc9ddc3757)
![6e46ed7d-0c8a-4dfd-8010-a1392723291f](https://github.com/user-attachments/assets/6cef05ec-3f3f-4043-a7cc-695de9130b6d)

for chatbot
![image](https://github.com/user-attachments/assets/2eec5a12-1c41-4b46-975f-3311923cbfe8)
![image](https://github.com/user-attachments/assets/74b9d350-e33a-4f02-b1f2-b62dcdfece02)
![image](https://github.com/user-attachments/assets/0c94a940-6a0d-48b5-a537-601314c6969e)

![image](https://github.com/user-attachments/assets/45ad0e2e-d085-4e77-96ea-baf11e064ff5)
![image](https://github.com/user-attachments/assets/e0e5b391-af4a-4455-85a7-9e36798e42e7)
![image](https://github.com/user-attachments/assets/716095c3-f4d3-4e2f-bf68-3175605a38d3)

for lungcancer
![image](https://github.com/user-attachments/assets/5d5554f2-ff36-4866-8ac1-d182c4116713)
![image](https://github.com/user-attachments/assets/ecdb6a4f-c718-418c-ada4-320eeb723cdb)
![image](https://github.com/user-attachments/assets/71666aa5-be5b-407f-89a0-a8fd5a333a4f)
![image](https://github.com/user-attachments/assets/18c38ed9-e1f5-445d-a169-a4ebd2343213)









---

