
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
import google.generativeai as genai
import os
import PIL.Image
import base64
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
import os
import requests
from django.core.files.storage import FileSystemStorage
# views.py
import os
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse

history = []
# Configure Gemini API
google_api_key = 'AIzaSyDPUUCaXw0iFJdjqbsVnsAcTJJpmBEF6t0'
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
   You are a domain expert in medical image analysis, tasked with examining both medical images and accompanying text descriptions for a renowned hospital. Your expertise will help in identifying or discovering any anomalies, diseases, conditions, or health issues that might be present in the image, as well as understanding and analyzing the textual information provided by the user.

Your key responsibilities:
1. **Detailed Analysis**: Scrutinize and thoroughly examine the provided image, focusing on finding any abnormalities. Also, consider the user's text description (if provided) to assist in your analysis.
2. **Analysis Report**: Document all findings from both the image and text input in a structured format.
3. **Recommendations**: Based on the analysis of both the image and text, suggest any remedies, tests, or treatments as applicable.
4. **Treatments**: If applicable, lay out detailed treatments that can help in faster recovery.

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
    
    Please provide the final response with these 4 headings : 
    Detailed Analysis, Analysis Report, Recommendations and Treatments

Please provide the final response with these 4 headings: Detailed Analysis, Analysis Report, Recommendations, and Treatments.

"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=system_prompt
)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment/register.html')  # Redirect to home or another page after registration
    else:
        form = RegistrationForm()
    return render(request, 'appointment/register.html', {'form': form})
# View function for analyzing images and/or text

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
                context['analysis'] = response.text

            # Clean up the temporary file
            os.remove(image_path)
        elif user_input:
            # If only text is provided, process the text input
            chat_session = model.start_chat(history=history)
            response = chat_session.send_message(user_input)
            model_response = response.text

            # Append user and bot messages to the history
            history.append({"role": "user", "parts": [user_input]})
            history.append({"role": "model", "parts": [model_response]})

            # Return JSON response for the bot's reply
            context['message'] = history
            return JsonResponse({'bot_response': model_response, 'history': history})
        
        else:
            # If neither image nor text is provided, show an error message
            context['error'] = "Please provide an image or text input for analysis."

    return render(request, 'appointment/analyze_image.html', context)
