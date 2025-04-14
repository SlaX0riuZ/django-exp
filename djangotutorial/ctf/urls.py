from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Home page
    path('challenges/', views.challenges, name='challenges'),
    path('challengesform/', views.challengesform, name='challengesform'),
    path('participants/', views.participants, name='participants'),
]