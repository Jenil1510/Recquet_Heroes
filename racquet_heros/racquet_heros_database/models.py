from django.db import models

# Create your models here.

class timezones(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    label_text = models.CharField(max_length=50)
    offset_in_seconds = models.BigIntegerField()

    class Meta:
        verbose_name_plural = "timezones"

class countries(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    flag = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=50, unique=True)
    default_timezone_id = models.ForeignKey(timezones, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "countries"

class cities(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    country_id = models.ForeignKey(countries, on_delete=models.SET_NULL, null=True)
    timezone_id = models.ForeignKey(timezones, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "cities"

class sports(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=300, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "sports"

class sport_format(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    sport_id = models.ForeignKey(sports, on_delete=models.SET_NULL, null=True)
    can_play_doubles = models.BooleanField(null=True)
    can_play_singles = models.BooleanField(null=True)
    default_set_count = models.BigIntegerField(default=1)
    default_game_count = models.BigIntegerField(default=3)
    default_set_score = models.BigIntegerField(default=0)
    default_set_duration_in_mins = models.BigIntegerField()
    is_from_tennis_family = models.BooleanField()

    class Meta:
        verbose_name_plural = "sport_format"