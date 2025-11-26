from django.db import models

class Appointment(models.Model):
    client_name = models.CharField(max_length=100)
    service = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client_name} - {self.service}"
