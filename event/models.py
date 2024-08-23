from django.db import models

class Events(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Event_Cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Title