from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from .models import EmergencyContact



def account(request):
    contacts=EmergencyContact.objects.filter(user=request.user)
    return render(request, 'account.html',{"contacts":contacts})

def emergency(request):
    send_mail(
    'Subject',
    'Message',
    'camranekeh@yahoo.com',
    ['camraneke.harden@thenobleacademy.org'],
    fail_silently=False


    )
    return HttpResponse(status=200)
# Create your views here.
