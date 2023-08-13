from django.urls import path
from . import views

urlpatterns = [
    path('', views.symptom_checker, name='symptom_checker'),
    path('disease/<int:disease_id>/', views.disease_detail, name='disease_detail'),
]
