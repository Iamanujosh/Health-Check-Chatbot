
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
import google.generativeai as genai
import os
import base64
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import os
import requests
from django.core.files.storage import FileSystemStorage
import os
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import RegisterForm,AppointmentForm
from .models import UserProfile,Doctor,Appointment
from django.urls import reverse
import pandas as pd
from .vital_analysis_model import predict_risk_with_ml, train_ml_model, generate_issues_report



history = []
# Example: Fetching user data from the database

# Configure Gemini API
# Example mapping
symptom_doctor_mapping = {
    "stomach hurting": "Dr. Smith",
    "headache": "Dr. Johnson",
    "fever": "Dr. Williams",
    # Add more symptoms and corresponding doctors
}

google_api_key = 'AIzaSyAmb11uMRSOS9sAwFSqZbJaOqmFrDpsxTM'
genai.configure(api_key=google_api_key)

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_prompt = """
  
   You are a domain expert in medical image analysis, tasked with examining both medical images and accompanying text descriptions for a renowned hospital.  Your expertise will help in identifying or discovering any anomalies, diseases, conditions, or health issues that might be present in the image, as well as understanding and analyzing the textual information provided by the user.



Your key responsibilities:
1.**Greeting user1**: you have to greet user user1 first and asked her about her disease which is cancer and solve her queries and provide insights on images.
2. **Detailed Analysis**: Scrutinize and thoroughly examine the provided image, focusing on finding any abnormalities. Also, consider the user's text description (if provided) to assist in your analysis.
3. **Analysis Report**: Document all findings from both the image and text input in a structured format.
4. **Recommendations**: Based on the analysis of both the image and text, suggest any remedies, tests, or treatments as applicable.
5. **Treatments**: If applicable, lay out detailed treatments that can help in faster recovery.
6. **Response format**: you have to include headings , breaks, paragraphs,and emojis for clean text.
7.**Appointment**: if user mentions any disease then just tell him that i have find you this doctor.

Important Notes to remember:
    1. Scope of response : Only respond if the image or input text pertains to 
    human health issues.
    2. Clarity of image : In case the image is unclear, 
    note that certain aspects are 
    'Unable to be correctly determined based on the uploaded image'
    3. Disclaimer : Accompany your analysis with the disclaimer: 
    "Consult with a Doctor before making any decisions."
    4. Your insights are invaluable in guiding clinical decisions. 
    Please proceed with the analysis, adhering to the 
    structured approach outlined above.
    5.Response format: you have to include headings , breaks, paragraphs,and emojis for clean text.
    
    
    Please provide the final response with these 2 headings in bold:  Recommendations, in new paragraph and Treatments.



"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=system_prompt
)
def home(request):
    return render(request, 'appointment/home.html')  # Ensure 'homepage.html' matches your HTML file's name
@login_required
def profile(request):
    # Access the logged-in user
    profile = UserProfile.objects.get(user=request.user)
    disease = profile.disease
    return render(request, 'appointment/profile.html', {'user': profile,'disease':disease})

def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            disease = form.cleaned_data.get('disease')

            # Save the disease in the UserProfile model
            UserProfile.objects.create(user=user, disease=disease)

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')  # Replace with your home page URL
    else:
        form = forms.RegisterForm()
    
    return render(request, 'appointment/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('analyze_image')  # Replace with your home view name
    else:
        form = AuthenticationForm()
    return render(request, 'appointment/login.html', {'form': form})


@login_required
def analyze_image(request):
    context = {}

    if request.method == "POST":
        image_file = request.FILES.get('image', None)
        user_input = request.POST.get('user_input', None)

        # Check if an image was uploaded
        if image_file:
            # Save the uploaded image temporarily
            image_path = default_storage.save(f"temp/{image_file.name}", image_file)
            
            with open(image_path, "rb") as image:
                image_data = image.read()

            # Encode image data to Base64
            image_data_base64 = base64.b64encode(image_data).decode('utf-8')

            # Prepare image part
            image_part = {
                "mime_type": image_file.content_type,  # Ensure correct MIME type
                "data": image_data_base64  # Use Base64-encoded string
            }

            prompt_parts = [image_part, system_prompt] if not user_input else [user_input, image_part, system_prompt]

            # Generate response using the model
            response = model.generate_content(prompt_parts)
            
            if response:
                # Format the bot's response into structured HTML
                formatted_response = f"""
                    <h3>🤖 Bot Analysis:</h3>
                    <p>{response.text}</p>
                    <h4>🔍 Key Insights:</h4>
                    <ul>
                        <li>🔸 Point 1: {response.point_1 if hasattr(response, 'point_1') else 'N/A'}</li>
                        <li>🔸 Point 2: {response.point_2 if hasattr(response, 'point_2') else 'N/A'}</li>
                        <li>🔸 Point 3: {response.point_3 if hasattr(response, 'point_3') else 'N/A'}</li>
                    </ul>
                    <p>For further assistance, please upload more information or ask another question! 😊</p>
                """
                return JsonResponse({'bot_response': formatted_response})

            # Clean up the temporary file
            os.remove(image_path)
        elif user_input:

            rec_doc = analyze_user_input(user_input)
            if rec_doc:
                context['doctor_card'] = {
                    'id': rec_doc.id,
                    'name': rec_doc.name,
                    'specialization': rec_doc.specialization,
                    'contact': rec_doc.contact_number,
                    "appointment_url": reverse('book_appointment', args=[rec_doc.id]),
                     # Assuming there's an image field
                }
            else:
                context['message'] = "No matching symptoms found. Please provide more details."
    
            
            chat_session = model.start_chat(history=history)
            response = chat_session.send_message(user_input)
            model_response = response.text

            # Append user and bot messages to the history
            history.append({"role": "user", "parts": [user_input]})
            history.append({"role": "model", "parts": [model_response]})

            # Return JSON response for the bot's reply
            context['message'] = history
            print(history)
            print("Doctor Card:", context.get('doctor_card'))  # Debug output

            return JsonResponse({
                'bot_response': model_response,
                'doctor_card': context.get('doctor_card'),  # Doctor details if found
                'history': history
            })
        
        else:
            # If neither image nor text is provided, show an error message
            context['error'] = "Please provide an image or text input for analysis."

    return render(request, 'appointment/analyze_image.html', context)



def analyze_user_input(user_input):
    # Convert input to lowercase for easier comparison
    input_lower = user_input.lower()

    # List of symptoms
    symptoms = [
        "stomach pain",
        "headache",
        "fever",
        "cough",
        "chest pain",
        "fatigue",
        "shortness of breath",
        "back pain",
        "nausea",
        "dizziness",
        "joint pain",
        "skin rash",
        "cold",
        "insomnia",
        "anxiety",
        "urinary problems",
        "weight loss",
        "vision changes",
        "hearing loss",
        "allergic reactions"
    ]

    # Loop through symptoms to find a match
    for symptom in symptoms:
        if symptom in input_lower:
            # Find the recommended doctor based on the symptom
            recommended_doctor = Doctor.objects.filter(specialization__icontains=symptom).first()
            return recommended_doctor  # Return the matched doctor

    return None  # No matching symptom found

def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.doctor = doctor
            appointment.save()
            return redirect('analyze_image')  # Redirect to a success page or the doctor profile
    else:
        form = AppointmentForm()

    return render(request, 'appointment/book_appointment.html', {'doctor': doctor, 'form': form})

def booking_success(request, doctor_id):
    # Assuming you have logic to get doctor and appointment details
    dr = Doctor.objects.get(id=doctor_id)
    appointment_date = dr.appointment_date  # Replace with actual appointment date
    appointment_time =dr.appointment_time   # Replace with actual appointment time

    context = {
        'doctor': dr,
        'appointment_date': appointment_date,
        'appointment_time': appointment_time,
    }

    return render(request, 'booking_success.html', context)

def vital_analysis(request):
    result = None
    issues_report = None

    if request.method == 'POST':
        heart_rate = int(request.POST['heart_rate'])
        respiratory_rate = int(request.POST['respiratory_rate'])
        body_temperature = float(request.POST['body_temperature'])
        oxygen_saturation = int(request.POST['oxygen_saturation'])
        systolic_blood_pressure = int(request.POST['systolic_blood_pressure'])
        diastolic_blood_pressure = int(request.POST['diastolic_blood_pressure'])

        # Load the trained model (ensure you train the model only once)
        model = train_ml_model()  # Make sure this function checks if the model is already trained.

        # Make the prediction
        risk_category_num = predict_risk_with_ml(
            model,
            heart_rate,
            respiratory_rate,
            body_temperature,
            oxygen_saturation,
            systolic_blood_pressure,
            diastolic_blood_pressure
        )

        # Determine risk category
        result = "High Risk" if risk_category_num == 1 else "Low Risk"

        # Generate a report based on the prediction
        issues_report = generate_issues_report(result)

    return render(request, 'appointment/vital_analysis.html', {'result': result, 'issues_report': issues_report})
