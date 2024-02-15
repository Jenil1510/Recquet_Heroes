from django.contrib import admin
from .models import timezones, countries, cities
# Register your models here.

admin.site.register(timezones)
admin.site.register(countries)
admin.site.register(cities)