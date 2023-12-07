from django.core.exceptions import ValidationError
from django.db import models

def validate_quantity_range(value):
    if value < 0 or value > 100:
        raise ValidationError('Quantity must be between 0 and 100 (inclusive).')

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(validators=[validate_quantity_range])

    def __str__(self):
        return self.name
