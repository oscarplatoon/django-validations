from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as text
from django.utils import timezone


def validate_first_name(first_name):
    if len(first_name) < 1:
        raise ValidationError(text('This field cannot be blank.'))

def validate_last_name(last_name):
    if len(last_name) < 1:
        raise ValidationError(text('This field cannot be blank.'))

def validate_team_name(team_name):
    if len(team_name) < 1:
        raise ValidationError(text('This field cannot be blank.'))


def validate_relay(relay):
    
    if relay == True or relay == False:
        raise ValidationError(text("'None' value must be either True or False."))

def validate_stroke(stroke):
    my_stroke = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']

    for each_stroke in my_stroke:
        if stroke is not my_stroke:
            raise ValidationError(text(f"{stroke} is not a valid stroke"))

def validate_distance(distance):
    
        if distance < 50:
            raise ValidationError(text("Ensure this value is greater than or equal to 50."))

def validate_time(time):
    
        if time > timezone.now():
            raise ValidationError(text("Can't set record in the future."))

def validate_record_time(record_time):
    
        if record_time < timezone.now():
            raise ValidationError(text("Can't break record before record was set."))

class SwimRecord(models.Model):

    first_name = models.CharField(max_length=64, validators=[validate_first_name])
    last_name = models.CharField(max_length=64, validators=[validate_last_name])
    team_name = models.CharField(max_length=64, validators=[validate_team_name])
    relay = models.BooleanField(validators=[validate_relay])
    stroke = models.CharField(max_length=64, validators=[validate_stroke])
    distance = models.IntegerField(validators=[validate_distance])
    record_date = models.DateTimeField(validators=[validate_time])
    record_broken_date = models.DateTimeField(validators=[validate_record_time])
