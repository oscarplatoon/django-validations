from datetime import datetime
from django import test
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

# Resolves test 5
def validate_stroke(value):
    valid_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if value not in valid_strokes:
        raise ValidationError(f"{value} is not a valid stroke")

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    team_name = models.CharField(max_length=200, null=False)
    relay = models.BooleanField(null=False)
    stroke = models.CharField(max_length=200, null=False, validators=[validate_stroke])
    distance = models.IntegerField()
    record_date = models.DateTimeField()
    record_broken_date = models.DateTimeField()

