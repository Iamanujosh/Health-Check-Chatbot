from django.db import models
from django.contrib.auth.models import User

# UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100, blank=True, null=True)  # Field for disease

    def __str__(self):
        return self.user.username

# Doctor model
class Doctor(models.Model):
    name = models.CharField(max_length=100, default='null')  # Default name is 'null'
    specialization = models.CharField(max_length=100, default='General Practitioner')  # Default specialization
    experience = models.IntegerField(default=1)  # Default experience set to 1 year
    contact_number = models.CharField(max_length=15, default='0000000000')  # Default contact number
    email = models.EmailField(default='doctor@example.com')  # Default email
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)  # Make image optional

    def __str__(self):
        return self.name

# Appointment model
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()  # Default to the current date/time
    reason = models.TextField(default="General consultation")  # Default reason for appointment

    def __str__(self):
        return f"Appointment with {self.doctor.name} for {self.user.username}"
