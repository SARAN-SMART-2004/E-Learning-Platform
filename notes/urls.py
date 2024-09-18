from django.urls import path
from . import views


urlpatterns = [
    

    path('notes/', views.list_notes, name='list_notes'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/delete/<int:note_id>/',  views.delete_note, name='delete_note'),
]