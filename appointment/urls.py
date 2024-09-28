from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_image, name='analyze_image'),
    path('register/',views.register,name='register')
]
