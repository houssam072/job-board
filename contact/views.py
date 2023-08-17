from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Info

# Create your views here.

def send_message(request):
    myInfo = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )


    return render(request,'contact/contact.html', {'myInfo':myInfo})
