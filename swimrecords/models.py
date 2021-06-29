from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.utils import timezone

class SwimRecord(models.Model):
    pass # delete me when you start writing in validations

    def validate_stroke(input):

        stroke_choices = ('front crawl', 'butterfly', 'breast', 'back', 'freestyle')
        if input not in stroke_choices:
            raise ValidationError('doggie paddle is not a valid stroke')

    def validate_record_date(input):

        if input > timezone.now():
            raise ValidationError("Can't set record in the future.")

    # @classmethod
    def validate_broken_date(input):

        if input < SwimRecord.record_date:
            raise ValidationError("Can't break record before record was set.")

    first_name = models.CharField(max_length=150,blank=False)
    
    last_name = models.CharField(max_length=150,blank=False)

    team_name = models.CharField(max_length=150,blank=False)

    relay = models.BooleanField(null=False)

    stroke = models.CharField(max_length=150, validators=[validate_stroke])

    distance = models.IntegerField(validators=[MinValueValidator(50, "Ensure this value is greater than or equal to 50.")])

    record_date = models.DateTimeField(validators=[validate_record_date])

    record_broken_date = models.DateTimeField(validators=[validate_broken_date])
