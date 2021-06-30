from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text
from django.utils import timezone


def not_null(input):
    if input == None:
        raise ValidationError(text('This field cannot be blank.'))

def true_false(input):
    if not(input == True or input == False):
        raise ValidationError(text(f"'{input}' value must be either True or False."))

def accepted_stroke(input):
    if input not in ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']:
        raise ValidationError(text(f"{input} is not a valid stroke"))

def distance(input):
    if not(input >= 50):
        raise ValidationError(text('Ensure this value is greater than or equal to 50.'))

def future_date(input):
    if input > timezone.now():
        raise ValidationError(text("Can't set record in the future."))
    
def record_break_before_initial_set(input):
    if record == None:
        raise ValidationError(text("Can't break record before record was set."))

    
class SwimRecord(models.Model):
    #create an instance of fullclean() in order to have access to broken record 

    first_name = models.CharField(max_length=255, validators=[not_null])
    last_name = models.CharField(max_length=255, validators=[not_null])
    team_name = models.CharField(max_length=255, validators=[not_null])
    relay = models.BooleanField(validators=[true_false])
    stroke = models.CharField(max_length=255, validators=[accepted_stroke])
    distance = models.IntegerField(validators=[distance])
    record_date = models.DateTimeField(validators=[future_date])
    record_broken_date = models.DateTimeField(validators=[record_break_before_initial_set])
