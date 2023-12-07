from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default='Default Description')
    quantity = models.IntegerField(default=0)  # Set the default value

    def __str__(self):
        return self.name
