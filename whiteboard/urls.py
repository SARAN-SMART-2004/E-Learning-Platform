# whiteboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('white/', views.whiteboard, name='whiteboard'),
]
