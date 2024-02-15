from django.db import models

# Create your models here.

class timezones(models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length = 200, unique = True)
    label_text = models.CharField(max_length = 50)
    offset_in_seconds = models.BigIntegerField()

    class Meta:
        verbose_name_plural = "timezones"

class countries(models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length = 200)
    flag = models.CharField(max_length = 50, null = True)
    code = models.CharField(max_length =50, unique = True)
    default_timezone_id = models.ForeignKey(timezones, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "countries"

class cities(models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    country_id = models.ForeignKey(countries, on_delete = models.CASCADE)
    timezone_id = models.ForeignKey(timezones, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "cities"

class sports(models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length = 300, unique = True)