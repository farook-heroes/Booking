from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Adjust the max_length as needed
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
   

    def __str__(self):
        return f"Booking for {self.name} on {self.date}"