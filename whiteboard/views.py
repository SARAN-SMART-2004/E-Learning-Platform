# whiteboard/views.py
from django.shortcuts import render

def whiteboard(request):
    return render(request, 'whiteboard.html')
