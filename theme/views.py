# views.py (in your_app_name)

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render a template called 'home.html'



def sign_up(request):
    return render(request, 'signup.html')


def library(request):
    return render(request, 'library.html')