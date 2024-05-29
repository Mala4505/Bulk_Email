# email_app/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest

def send_bulk_email_view(request):
    if request.method == 'POST':
        recipients = request.POST.get('recipients')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        
        if not recipients or not subject or not body:
            return HttpResponseBadRequest('All fields are required.')

        recipient_list = [email.strip() for email in recipients.split(',')]
        
        if not recipient_list:
            return HttpResponseBadRequest('Recipient list is empty.')

        try:
            # Send emails in a loop
            for recipient in recipient_list:
                send_mail(subject, body, 'your_email', [recipient])
            return HttpResponse('Bulk email(s) sent successfully!')
        except Exception as e:
            return HttpResponseBadRequest(f'Error sending emails: {e}')
    else:
        return render(request, 'send_bulk_email.html')
