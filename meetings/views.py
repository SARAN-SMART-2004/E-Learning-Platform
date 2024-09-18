from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

@csrf_exempt
def meeting(request):
    if request.method == 'POST':
        # Handle the AJAX request
        data = json.loads(request.body)
        meeting_id = data.get('meeting_id')

        # Fetch email addresses of users (example)
        user_emails = ['saran152004s@gmail.com', 'smartsaran3031@gmail.com']

        # Prepare email content
        subject = 'New Meeting ID'
        message = f'You have a new meeting ID: {meeting_id}'
        from_email = 'travelcrewservice@gmail.com'

        # Send email to each user
        for email in user_emails:
            send_mail(subject, message, from_email, [email])

        return JsonResponse({'status': 'success', 'meeting_id': meeting_id})
    
    # Handle the GET request to render the page
    return render(request, 'meetings/index.html')
