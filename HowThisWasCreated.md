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