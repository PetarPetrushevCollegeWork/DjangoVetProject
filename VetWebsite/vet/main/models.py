from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Service(TimeStampedModel):
	name = models.CharField(max_length=120)
	description = models.TextField(blank=True)
	duration_minutes = models.PositiveIntegerField(default=30)
	price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Client(TimeStampedModel):
	name = models.CharField(max_length=120)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=40, blank=True)
	address = models.CharField(max_length=255, blank=True)
	notes = models.TextField(blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Pet(TimeStampedModel):
	class Species(models.TextChoices):
		DOG = 'dog', 'Dog'
		CAT = 'cat', 'Cat'
		BIRD = 'bird', 'Bird'
		RABBIT = 'rabbit', 'Rabbit'
		OTHER = 'other', 'Other'

	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='pets')
	name = models.CharField(max_length=120)
	species = models.CharField(max_length=20, choices=Species.choices, default=Species.DOG)
	breed = models.CharField(max_length=120, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	notes = models.TextField(blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f'{self.name} ({self.client.name})'


class Lead(TimeStampedModel):
	class Status(models.TextChoices):
		NEW = 'new', 'New'
		CONTACTED = 'contacted', 'Contacted'
		BOOKED = 'booked', 'Booked'
		WON = 'won', 'Won'
		LOST = 'lost', 'Lost'

	class Source(models.TextChoices):
		WEBSITE = 'website', 'Website'
		PHONE = 'phone', 'Phone'
		REFERRAL = 'referral', 'Referral'
		WALK_IN = 'walk_in', 'Walk-in'
		SOCIAL = 'social', 'Social'

	name = models.CharField(max_length=120)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=40, blank=True)
	source = models.CharField(max_length=20, choices=Source.choices, default=Source.WEBSITE)
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
	interested_service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')
	notes = models.TextField(blank=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'{self.name} - {self.get_status_display()}'


class Appointment(TimeStampedModel):
	class Status(models.TextChoices):
		SCHEDULED = 'scheduled', 'Scheduled'
		CHECKED_IN = 'checked_in', 'Checked In'
		COMPLETED = 'completed', 'Completed'
		CANCELLED = 'cancelled', 'Cancelled'

	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')
	pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
	scheduled_for = models.DateTimeField()
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)
	assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')
	notes = models.TextField(blank=True)

	class Meta:
		ordering = ['scheduled_for']

	def __str__(self):
		return f'{self.client.name} - {self.scheduled_for:%d %b %Y %H:%M}'
