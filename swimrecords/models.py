from datetime import date
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import NullBooleanField
from django.core.validators import MinValueValidator
from django.utils import timezone

# Write functions here!

# Stroke validator
def validate_stroke(stroke):
    stroke_list = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in stroke_list:
        raise ValidationError(f"{stroke} is not a valid stroke")

# Future Date validator
def date_checker(test_date):
    if test_date > timezone.now():
        raise ValidationError("Can't set record in the future.")

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    team_name = models.CharField(max_length=100, null=False)
    relay = models.BooleanField(null=False)
    stroke = models.CharField(max_length=100, validators=[validate_stroke])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[date_checker])
    record_broken_date = models.DateTimeField()

    # Record broken validator
    def clean(self):
        cleaned_data = super().clean()
        if self.record_date and self.record_broken_date:
            if self.record_date >= self.record_broken_date:
                raise ValidationError({'record_broken_date':"Can't break record before record was set."})