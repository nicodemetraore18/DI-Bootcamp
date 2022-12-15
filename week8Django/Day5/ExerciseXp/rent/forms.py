from django import forms
from .models import Customer,Rental,Vehicle

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','email','phone_number','address','city','country']


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['return_date','customer','vehicle']
        widgets = {
            'return_date':forms.SelectDateWidget(),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type','real_cost','size']

