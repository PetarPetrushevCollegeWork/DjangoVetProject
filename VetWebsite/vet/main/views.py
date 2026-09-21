from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    form = UserCreationForm()

    return render(request, "register.html", {"form": form})