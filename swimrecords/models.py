from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *
from datetime import timedelta
from django.utils import timezone

def validate_stroke(input_stroke):
    valid_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if input_stroke not in valid_strokes:
        raise ValidationError(f"{input_stroke} is not a valid stroke")

def validate_date(input_date):
    if input_date > timezone.now():
        raise ValidationError("Can't set record in the future.")

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    team_name = models.CharField(max_length=255, null=False)
    relay = models.BooleanField(null=False)
    stroke = models.CharField(max_length=14, validators=[validate_stroke])
    distance = models.IntegerField(validators=[MinValueValidator(50, "Ensure this value is greater than or equal to 50.")])
    record_date = models.DateTimeField(validators=[validate_date])
    record_broken_date = models.DateTimeField()

    def clean(self):
        super().clean()
        if self.record_broken_date and self.record_date and self.record_broken_date < self.record_date:
            raise ValidationError({'record_broken_date':"Can't break record before record was set."})