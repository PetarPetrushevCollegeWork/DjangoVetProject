from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):

    # dynamic content
    context = {"clinic_name": "Happy Paws 🐾",
               "tagline": "Your fiendly vet",
               "services": ["Check-ups","X rays", "Dentistry","Vaccinations"]
               }

    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")