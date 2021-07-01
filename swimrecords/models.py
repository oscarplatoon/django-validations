from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as text
from django.utils import timezone



def accepted_stroke(input):
    if input not in ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']:
        raise ValidationError(text(f"{input} is not a valid stroke"))

def distance(input):
    if not(input >= 50):
        raise ValidationError(text('Ensure this value is greater than or equal to 50.'))

def future_date(input):
    if input > timezone.now():
        raise ValidationError(text("Can't set record in the future."))
    

    
class SwimRecord(models.Model):
    #create an instance of fullclean() in order to have access to broken record 

    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    team_name = models.CharField(max_length=255, null = True)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=255, validators=[accepted_stroke])
    distance = models.IntegerField(validators=[distance])
    record_date = models.DateTimeField(validators=[future_date])
    record_broken_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.record_broken_date > self.record_date:
            raise ValidationError(text("Can't break record before record was set."))
        super().save(*args, **kwargs)
