from django.urls import path
from . import views

urlpatterns = [
    path('courselist/', views.course_list, name='course_list'),
    # path('course/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('search/', views.search_courses, name='search_courses'),
    path('<int:course_id>/delete/', views.course_delete, name='course_delete'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:pk>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('course/<int:course_id>/submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('course/<int:course_pk>/remove_student/<int:user_pk>/', views.remove_student, name='remove_student'),
    path('myteaching/',views.myteaching,name='myteaching'),
    path('add-course/', views.add_course, name='add_course'),
]

 