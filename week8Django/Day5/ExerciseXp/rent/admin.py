from django.contrib import admin

# Register your models here.
from .models import Customer,Vehicle,Vehicle_Type,Vehicle_Size,Rental,Rental_Rate


admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Vehicle_Type)
admin.site.register(Vehicle_Size)
admin.site.register(Rental)
admin.site.register(Rental_Rate)