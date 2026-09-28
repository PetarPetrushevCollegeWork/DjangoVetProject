from django.contrib import admin
from .models import Appointment, Client, Lead, Pet, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'duration_minutes', 'price', 'featured', 'active')
	list_filter = ('featured', 'active')
	search_fields = ('name', 'description')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'created_at')
	search_fields = ('name', 'email', 'phone')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	list_display = ('name', 'species', 'breed', 'client')
	list_filter = ('species',)
	search_fields = ('name', 'breed', 'client__name')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	list_display = ('name', 'source', 'status', 'interested_service', 'created_at')
	list_filter = ('source', 'status')
	search_fields = ('name', 'email', 'phone')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('client', 'pet', 'service', 'scheduled_for', 'status', 'assigned_to')
	list_filter = ('status', 'service')
	search_fields = ('client__name', 'pet__name', 'service__name')
	autocomplete_fields = ('client', 'pet', 'service', 'assigned_to')
