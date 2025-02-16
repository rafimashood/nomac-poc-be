"""Contains the Api endpoints for Analyze part"""
from django.urls import path
from . import views


urlpatterns = [
    path('analyze-data-blocks/', views.analyze_data_blocks, name='analyze_data_blocks'),
]
