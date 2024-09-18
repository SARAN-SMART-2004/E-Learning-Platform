from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm


def get_user_context(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        context.update({
            'current_user': current_user,
            'username': current_user.username,
            'email': current_user.email,
            'description': current_user.description,
            
            'image': current_user.image.url if current_user.image else None,
            'status': current_user.status,
            
        })
    return context

# Create your views here.
@login_required
def list_notes(request):
    context = get_user_context(request)
    notes = Note.objects.filter(user=request.user)
    context.update({
        'notes': notes, # Pass unique users to the context
    })
    return render(request, 'notes/list_notes.html', context)

@login_required
def add_note(request):
    context = get_user_context(request)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect('list_notes')
    else:
        form = NoteForm()
    context.update({
        'form': form, # Pass unique users to the context
    })
    return render(request, 'notes/add_note.html', context)

@login_required
def delete_note(request, note_id):
    context = get_user_context(request)
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('list_notes')
    context.update({
        'note': note, # Pass unique users to the context
    })
    return render(request, 'notes/confirm_delete.html', context)

