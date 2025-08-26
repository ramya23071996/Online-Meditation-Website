from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def therapy_view(request):
    return render(request, 'therapy.html')

def about_view(request):
    return render(request, 'about.html')

def meditation_view(request):
    return render(request, 'meditation.html')

def contact_view(request):
    return render(request, 'contact.html')

def trials_view(request):
    return render(request, 'trials.html')

def family_view(request):
    return render(request, 'family.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def approach_view(request):
    return render(request, 'approach.html')

def payment_view(request):
    return render(request, 'payment.html')