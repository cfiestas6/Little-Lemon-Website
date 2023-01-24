from django.db import models

# Create your models here.
class Booking(models.Model):
    name =  models.CharField(max_length=255, default='')
    no_of_guests = models.IntegerField(null=True)
    bookingdate = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(null=True, max_length=255)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    inventory = models.IntegerField(null=True)
    
    def __str__(self):
        return self.title