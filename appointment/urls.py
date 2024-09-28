from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('analyze_image/', views.analyze_image, name='analyze_image'),
    path('login/',views.login_view,name='login'),
    path('register/', views.register_view, name='register'),

]
