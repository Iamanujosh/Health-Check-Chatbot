from django.core.management.base import BaseCommand
from datasets import load_dataset
# Import any necessary libraries for training your model

class Command(BaseCommand):
    help = 'Train the NLP model with the appointment dataset'

    def handle(self, *args, **kwargs):
        # Load the dataset
        ds = load_dataset("Vishwaksen/AppointmentAssistant-V1")
        
        # Your model training logic here
       
        # Example: Preprocess data, train your model, etc.
        
        self.stdout.write(self.style.SUCCESS('Model training complete!'))
