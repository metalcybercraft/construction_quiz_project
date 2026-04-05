from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/<int:pk>/edit/', views.question_edit, name='question_edit'),
    path('quiz/', views.quiz_start, name='quiz_start'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
    path('about/', views.about, name='about'),
]