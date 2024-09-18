from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment,Feedback
from django.http import HttpResponseBadRequest
from django.contrib import messages
# from .forms import CourseForm
from .decorators import teacher_required


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
            'website_url': current_user.website_url,
            'twitter_profile': current_user.twitter_profile,
            'facebook_profile': current_user.facebook_profile,
            'linkedin_profile': current_user.linkedin_profile,
            'youtube_profile': current_user.youtube_profile,
            
            
        })
    return context
@login_required
def course_list(request):
    courses = Course.objects.all()
    context=get_user_context(request)
    context['courses'] = courses
    return render(request, 'course/course_list.html', context)




# @teacher_required
# @login_required
# def course_edit(request, pk):
#     course = get_object_or_404(Course, pk=pk)
    
#     # Check if the current user is the instructor
#     if course.instructor != request.user:
#         return HttpResponseForbidden("You are not allowed to edit this course.")

#     if request.method == 'POST':
#         form = CourseForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#             return redirect('course_detail', pk=pk)
#     else:
#         form = CourseForm(instance=course)

#     return render(request, 'course/course_edit.html', {
#         'form': form,
#         'course': course
#     })


@teacher_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.instructor != request.user:
        return HttpResponseForbidden("You cannot delete this course.")
    
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    
    return render(request, 'course/course_confirm_delete.html', {'course': course})

# @login_required
# def course_detail(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
#     is_instructor = course.instructor == request.user
    
#     if request.method == 'POST' and not is_instructor:
#         if not is_enrolled:
#             Enrollment.objects.create(user=request.user, course=course)
#             return redirect('course_detail', pk=pk)  # Redirect to avoid form resubmission
 
#     enrolled_students = Enrollment.objects.filter(course=course).select_related('user') if is_instructor else []

#     return render(request, 'course/course_detail.html', {
#         'course': course,
#         'is_enrolled': is_enrolled,
#         'is_instructor': is_instructor,
#         'enrolled_students': enrolled_students
#     })

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    is_creator = course.creator == request.user
    feedbacks = Feedback.objects.filter(course=course)
    enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    # Get the enrollment count for the course
    enrollment_count = Enrollment.objects.filter(course=course).count()
    context = {
        'course': course,
        'enrolled': enrolled,
        'is_creator': is_creator,
        'feedbacks': feedbacks,
        'enrollment_count': enrollment_count,
    }
    return render(request, 'course/course_detail.html', context)

@login_required
def enroll_in_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    # Check if the user is the instructor
    if course.creator == request.user:
        messages.error(request, f'You are the tutor of  {course.title}! so you cannot enroll')
    
    # Check if the user is already enrolled
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        Enrollment.objects.create(user=request.user, course=course)
        messages.success(request, f'You have successfully enrolled in {course.title}!')
    else:
        messages.info(request, f'You are already enrolled in {course.title}.')
    
    return redirect('course_detail', pk=pk)

@login_required
def remove_student(request, course_pk, user_pk):
    course = get_object_or_404(Course, pk=course_pk)
    
    # Check if the user is the instructor
    if course.instructor != request.user:
        return HttpResponseForbidden("You are not allowed to remove students from this course.")
    
    # Check if the user is enrolled in the course
    enrollment = Enrollment.objects.filter(course=course, user__pk=user_pk).first()
    if enrollment:
        enrollment.delete()
    
    return redirect('course_detail', pk=course_pk)
def myteaching(request):
    context=get_user_context(request)
    return render(request,'tutor/My_teaching.html',context)






from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .models import Course

@login_required
def add_course(request):
    if request.method == "POST":
        title = request.POST.get('course-title')
        content = request.POST.get('course-content')  # assuming you want to store content
        category = request.POST.get('category')
        tags = request.POST.get('tags')
        max_students = request.POST.get('max-students', 0)
        difficulty_level = request.POST.get('difficulty-level')
        is_public = request.POST.get('public-course', False)
        qa_enabled = request.POST.get('qa-enabled', False)
        course_benefits = request.POST.get('course-benefits')
        target_audience = request.POST.get('target-audience')
        course_duration_hours = request.POST.get('course-duration-hours', 0)
        course_duration_minutes = request.POST.get('course-duration-minutes', 0)
        materials_included = request.POST.get('materials-included')
        requirements = request.POST.get('requirements')
        video = request.FILES.get('video')

        # Save the course object
        course = Course(
            creator=request.user,
            title=title,
            content=content,
            category=category,
            tags=tags,
            max_students=max_students,
            difficulty_level=difficulty_level,
            is_public=is_public,
            qa_enabled=qa_enabled,
            course_benefits=course_benefits,
            target_audience=target_audience,
            course_duration_hours=course_duration_hours,
            course_duration_minutes=course_duration_minutes,
            materials_included=materials_included,
            requirements=requirements,
            video=video
        )
        course.save()
        
        return redirect('course/course_list', course_id=course.id)

    return render(request, 'course/createcourse.html')

def submit_feedback(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        
        if not all([name, email, rating, comments]):
            return HttpResponseBadRequest("All fields are required.")
        
        feedback = Feedback(
            course=course,
            user=request.user,
            name=name,
            email=email,
            rating=rating,
            comments=comments
        )
        feedback.save()
        messages.success(request, f'You have successfully Submitted feedback for {course.title}!')
        
        return redirect('course_list')  # Ensure 'course_detail' pattern uses 'course_id'
    else:
        return HttpResponseBadRequest("Invalid request method.")
    
from django.shortcuts import render
from .models import Course  # Import the Course model
from django.db.models import Q  # Import Q for complex lookups

def search_courses(request):
    query = request.GET.get('q', '')
    if query:
        # Use Q for OR conditions in filtering
        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(tags__icontains=query)
        )
    else:
        courses = Course.objects.all()

    context = {
        'courses': courses,
        'query': query,
    }
    return render(request, 'course/search_results.html', context)
