from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Home page
    path('challenges/', views.challenges, name='challenges'),
    path('challengesform/', views.challengesform, name='challengesform'),
    path('participants/', views.participants, name='participants'),
    path('challengecompletion/', views.submit_flag, name='challengecompletion'),
    path('challenges/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('startchallenge/<int:challenge_id>/', views.start_challenge, name='start_challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('register/', views.register, name='register'),
]