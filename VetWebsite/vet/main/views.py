from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {"clinic_name": "Happy Paws",
               "tagline": "your freindly vet :3",
               "services": ["Check-ups", "X-rays", "Dentistry", "Vaccinations"]}
    return render(request, "home.html", context)