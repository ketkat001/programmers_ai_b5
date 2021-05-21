from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'strock/home.html')


def age(request):
    return render(request, 'strock/age.html')


def bmi(request):
    return render(request, 'strock/bmi.html')


def smoking(request):
    return render(request, 'strock/smoking.html')