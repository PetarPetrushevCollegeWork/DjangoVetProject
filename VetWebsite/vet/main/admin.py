from django.contrib import admin
from .models import Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = (("pet_name","animal","date","time","owner"))

admin.site.register(Booking, BookingAdmin)