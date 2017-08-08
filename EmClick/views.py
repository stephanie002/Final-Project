from django.shortcuts import render
from .models import EmergencyContact



def account(request):
    contacts=EmergencyContact.objects.filter(user=request.user)
    return render(request, 'account.html',{"contacts":contacts})


# Create your views here.
