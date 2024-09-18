from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.homepage, name="homepage"),
    
    path("dashboard/", views.dashboard, name="dashboard"),
    path("coursedashboard/", views.coursedashboard, name="coursedashboard"),
    
    path('chatbot/',views.chatbot,name='chatbot'),   

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)