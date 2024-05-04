from django.urls import path
from . import views



urlpatterns = [
    path('', views.registrations, name='registration'),
    path('login/', views.login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
]
