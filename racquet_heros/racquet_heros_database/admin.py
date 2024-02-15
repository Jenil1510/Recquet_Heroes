from django.contrib import admin
from .models import timezones, countries, cities, sports, sport_format
# Register your models here.

admin.site.register(timezones)
admin.site.register(countries)
admin.site.register(cities)
admin.site.register(sports)
admin.site.register(sport_format)