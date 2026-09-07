# How this was created

## Exact steps used
1. python -m venv venv
2. pip install Django~=5.2
3. Create new folder called "VetWebsite"
4. pip freeze > requirements.txt
5. django-admin startproject vet
6. python manage.py runserver
7. python manage.py startapp main
8. Edit settings.py to add "main" app to installed apps.
9. Edit settings.py to change timezone to "Europe/London".
10. Edit settings.py to change language to "en-gb".
11. python manage.py check
12. python manage.py makemigrations
13. python manage.py migrate
14. add "from django.http import HttpResponse" to main/views.py
15. add 
> def home(request):
>     context = {"clinic_name": "Happy Paws",
>                "tagline": "your freindly vet :3",
>                "services": ["Check-ups", "X-rays", "Dentistry", "Vaccinations"]}
>     return render(request, "home.html", context)
to main/views.py
16. add "path("", views.home, name="home")" to vet/urls.py
17. add "from main import views" to vet/urls.py
18. update settings.py TEMPLATES "...'DIRS': [BASE_DIR / "templates"]..."
19. create folder called "templates" in /VetWebsite/vet/
20. Create home.html in the new templates folder.
> Use {{ clinic_name }} and {{ tagline }} inside.
> Also use:
> {% for service in services %}
>     <li>{{service}}</li>
> {% endfor %}