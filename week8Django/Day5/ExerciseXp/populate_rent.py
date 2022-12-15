import os
from datetime import datetime
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ExerciseXp.settings')

import django

django.setup()

import random
from rent.models import Customer,Rental,Vehicle_Type,Vehicle_Size,Vehicle,Rental_Rate

from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        first_name = fakegen.name()
        last_name = fakegen.name()
        email = fakegen.ascii_email()
        phone_number = fakegen.phone_number()
        address = fakegen.address()
        city = fakegen.city()
        country = fakegen.country()

        Custom = Customer.objects.get_or_create(first_name=first_name, last_name=last_name, email=email,phone_number=phone_number, address=address,country=country, city=city)[0]
        Custom.save()

def assertBetween( date, start_date, end_date):
        assert date.year <= end_date.year
        assert date.month > start_date.month
        return date

def populater(N=5):
    nbr_vehicle=Vehicle.objects.all().count()
    nbr_Customer = Customer.objects.all().count()
    nw=datetime.now()
    end_date=nw + timedelta(days = 365)

    for entry in range(N):
        okdate =fakegen.date_between_dates(nw,end_date)
        return_date = okdate
        customerid= random.randint(1, nbr_Customer)
        vehicleid = random.randint(1, nbr_vehicle)

        rent = Rental.objects.get_or_create(return_date=return_date, customer=Customer.objects.get(pk=customerid),vehicle=Vehicle.objects.get(pk=vehicleid))[0]
        rent.save()

if __name__ == '__main__':
    print("populating script!")
    populater(100)
    print("populating complete!")