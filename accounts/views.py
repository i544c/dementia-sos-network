from django.shortcuts import render
from django.contrib.auth.models import User

def profile(request):
    return render(request, 'accounts/profile.html')
