
# Gemini Health Care Chatbot

## Overview

The **Gemini Health Care Chatbot** is a Django-based healthcare assistant that helps patients analyze medical images and symptoms to identify potential health concerns. The bot provides detailed analysis, recommendations, and treatment options based on the provided input, whether it's a medical image or text description.

## Features

-   **User Registration and Login**: Allows users to register, log in, and maintain a personalized profile.
-   **Medical Image Analysis**: Patients can upload medical images, which the chatbot analyzes for abnormalities and potential health issues.
-   **Symptom Analysis**: Patients can describe their symptoms, and the chatbot will suggest possible conditions and provide advice.
-   **Doctor Recommendations**: Based on the user’s profile and symptoms, the bot suggests relevant doctors for appointment scheduling.
-   **Gemini AI Integration**: Powered by Gemini's AI for generating responses to the uploaded images or user queries.

## Technologies Used

-   **Backend**: Django
-   **Frontend**: HTML, CSS
-   **Database**: SQLite (default in Django) or other Django-supported databases
-   **API Integration**: Google Gemini API for medical image and symptom analysis

## Prerequisites

Before setting up the project, make sure you have the following installed:

-   Python 3.x
-   Django 4.x or later
-   Google Gemini API key


## Usage

1.  **Register and Login**: Users must register and log in to access the chatbot.
2.  **Profile Setup**: After login, users can access their profile to view personal information and their disease history.
3.  **Upload Medical Images**: On the **Analyze Image** page, users can upload medical images or input symptoms for the chatbot to analyze.
4.  **Receive Recommendations**: The chatbot will provide detailed analysis, reports, recommendations, and potential treatments based on the input.

## Directory Structure




## Models

### `UserProfile`

This model extends the default Django `User` model and stores additional information such as the user's disease history.

-   **Fields**:
    -   `user`: ForeignKey to `User`
    -   `disease`: TextField
## API Integration

The chatbot uses Google Gemini's Generative AI API to process medical images and textual inputs. The integration is managed in `views.py` where the image or text is sent to the Gemini model, and a detailed response is generated.

# Vitals Monitoring and Prediction System

## Overview

The **Vitals Monitoring and Prediction System** is a Python-based solution that assesses an individual's health risk based on their key vital signs. By collecting inputs such as heart rate, respiratory rate, body temperature, oxygen saturation, and blood pressure, the system utilizes a trained Logistic Regression model to categorize the user's health status into either **Low Risk** or **High Risk**. Additionally, it generates comprehensive reports summarizing the findings, aiding in proactive healthcare management.

## Features

-   **Vital Signs Collection**: Interactive input fields allow users to enter their heart rate, respiratory rate, body temperature, oxygen saturation, and blood pressure.
-   **Risk Prediction**: The system uses a trained Logistic Regression model to evaluate the risk category based on the provided vital signs.
-   **Automated Reporting**: A detailed text report (`patient_issues_report.txt`) is generated, summarizing the vital signs and the predicted risk category.
-   **Model Training and Persistence**: The system can load a dataset, train a machine learning model, evaluate its accuracy, and save the trained model for future predictions.
-   **Interactive Interface**: The project utilizes `ipywidgets` within a Jupyter Notebook for seamless and user-friendly data input and interaction.

## Technologies Used

-   **Programming Language**: Python 3.x
-   **Libraries and Frameworks**:
    -   **Data Handling**: `pandas`
    -   **Machine Learning**: `scikit-learn` (Logistic Regression), `joblib`
    -   **Interactive UI**: `ipywidgets`, `IPython.display`
    -   **File Operations**: `os`
-   **Environment**: Jupyter Notebook for interactive execution and documentation
