from datetime import datetime, timezone
from django.utils import timezone
from typing import ValuesView
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as text


def validate_first_name_presence(first):
        if len(first) == 0:
            raise ValidationError(text(
            'This field cannot be blank.')
            )

def validate_last_name_presence(last):
        if len(last) == 0:
            raise ValidationError(text(
            'This field cannot be blank.')
            )

def validate_team_name_presence(team):
        if len(team) == 0:
            raise ValidationError(text(
            'This field cannot be blank.')
            )

def valid_stroke(stroke):
    if stroke not in SwimRecord.objects.filter(stroke=stroke):
        raise ValidationError(
            text(f'{stroke} is not a valid stroke')
        )

def valid_distance(distance):
    if distance < 50:
        raise ValidationError(
            text("Ensure this value is greater than or equal to 50.")
        )
def no_future_records(record_date):

    if record_date >= timezone.now():
        raise ValidationError(text("Can't set record in the future.")) 

def no_break_record_before_set_record(record_broken_date):
    if record_broken_date < timezone.now():
        raise ValidationError(text("Can't break record before record was set."))

class SwimRecord(models.Model):

    first_name = models.CharField(max_length=200,validators=[validate_first_name_presence])

    last_name = models.CharField(max_length=200, validators=[validate_last_name_presence])

    team_name = models.CharField(max_length=200, validators=[validate_team_name_presence])

    relay = models.BooleanField()

    stroke = models.CharField(max_length=200, validators=[valid_stroke])

    distance = models.IntegerField(validators=[valid_distance])


    record_date = models.DateTimeField(validators=[no_future_records])

    record_broken_date = models.DateTimeField(validators=[no_break_record_before_set_record])
