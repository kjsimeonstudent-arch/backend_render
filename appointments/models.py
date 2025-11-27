from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient_name} - {self.date} {self.time}"
