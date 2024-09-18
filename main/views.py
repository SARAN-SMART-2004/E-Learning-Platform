
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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


def homepage(request):
    context = get_user_context(request)
     # Check if the celebration effect should be shown
    show_celebration = request.session.pop('show_celebration', False)

    
    # Add the celebration flag to the context
    context['show_celebration'] = show_celebration
    
    return render(request, 'main/design/header.html', context)
def chatbot(request):
    context = get_user_context(request)
    return render(request, 'main/chatbot.html', context)




def dashboard(request):
    context = get_user_context(request)
    return render(request, 'main/design/boxindex.html', context)
def coursedashboard(request):
    context = get_user_context(request)
    return render(request, 'main/includes/dashboard.html', context)
