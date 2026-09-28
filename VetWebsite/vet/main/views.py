from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from .models import Appointment, Client, Lead, Pet, Service


def _featured_services():
    services = list(Service.objects.filter(active=True, featured=True)[:3])
    if services:
        return services
    return [
        {
            'name': 'Preventive Check-ups',
            'description': 'Routine wellness exams that keep pets healthy and catch issues early.',
            'duration_minutes': 30,
            'price': '45.00',
        },
        {
            'name': 'Diagnostics',
            'description': 'Fast, clear insights through lab work, imaging, and in-clinic screening.',
            'duration_minutes': 45,
            'price': '90.00',
        },
        {
            'name': 'Dental Care',
            'description': 'Cleanings, oral health checks, and treatment plans for long-term comfort.',
            'duration_minutes': 60,
            'price': '120.00',
        },
    ]


def _sample_clients():
    return [
        {'name': 'Maya Carter', 'email': 'maya@example.com', 'phone': '+44 7700 900111', 'pet_count': 2, 'status': 'Active client'},
        {'name': 'Jordan Lee', 'email': 'jordan@example.com', 'phone': '+44 7700 900222', 'pet_count': 1, 'status': 'Follow-up due'},
        {'name': 'Aisha Khan', 'email': 'aisha@example.com', 'phone': '+44 7700 900333', 'pet_count': 3, 'status': 'Booked this week'},
    ]


def home(request):
    services = _featured_services()
    stats = {
        'clients': Client.objects.count() or 128,
        'pets': Pet.objects.count() or 214,
        'appointments': Appointment.objects.count() or 46,
        'leads': Lead.objects.count() or 18,
    }
    context = {
        'clinic_name': 'Happy Paws Veterinary',
        'tagline': 'A warm, modern clinic experience with patient records, CRM workflows, and staff-friendly tools.',
        'services': services,
        'stats': stats,
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'clinic_name': 'Happy Paws Veterinary',
        'highlights': [
            'Staff-friendly CRM with clients, pets, appointments, and leads in one place.',
            'Authenticated dashboard so the team can work with real operational data.',
            'A polished front end with stronger typography, motion, and responsive layout.',
        ],
    }
    return render(request, 'about.html', context)


@login_required
def dashboard(request):
    stats = {
        'clients': Client.objects.count(),
        'pets': Pet.objects.count(),
        'appointments': Appointment.objects.count(),
        'leads': Lead.objects.count(),
    }

    upcoming_appointments = list(
        Appointment.objects.select_related('client', 'pet', 'service', 'assigned_to').order_by('scheduled_for')[:5]
    )
    recent_clients = list(
        Client.objects.annotate(pet_count=Count('pets')).order_by('-created_at')[:5]
    )
    recent_leads = list(
        Lead.objects.select_related('interested_service').order_by('-created_at')[:5]
    )

    if not recent_clients:
        recent_clients = _sample_clients()

    context = {
        'stats': stats,
        'upcoming_appointments': upcoming_appointments,
        'recent_clients': recent_clients,
        'recent_leads': recent_leads,
    }
    return render(request, 'dashboard.html', context)


@login_required
def clients(request):
    query = request.GET.get('q', '').strip()
    clients_qs = Client.objects.annotate(pet_count=Count('pets')).order_by('name')
    if query:
        clients_qs = clients_qs.filter(name__icontains=query) | clients_qs.filter(email__icontains=query) | clients_qs.filter(phone__icontains=query)

    clients_list = list(clients_qs.distinct()[:20])
    if not clients_list:
        clients_list = _sample_clients()

    return render(request, 'clients.html', {'clients': clients_list, 'query': query})