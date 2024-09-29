from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/',views.profile,name='profile'),
    path('analyze_image/', views.analyze_image, name='analyze_image'),
    path('login/',views.login_view,name='login'),
    path('register/', views.register_view, name='register'),
    path('book-appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('vital-analysis/', views.vital_analysis, name='vital_analysis'),
]
