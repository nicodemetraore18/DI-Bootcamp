from django.db import models
from djmoney.models.fields import MoneyField

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.first_name

class Vehicle_Type(models.Model):
        name = models.CharField(max_length=50, blank=True)

        def __str__(self):
            return self.name


class Vehicle_Size(models.Model):
    name = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_Type,   on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now = True)
    real_cost =MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )
    size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)



class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now = True)
    return_date = models.DateTimeField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,   on_delete=models.CASCADE)
    def __str__(self):
        return str(self.rental_date)


class Rental_Rate(models.Model):
    daily_rate = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )
    vehicle_type= models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    Vehicle_Size= models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.daily_rate)

