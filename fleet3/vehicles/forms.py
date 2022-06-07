
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from vehicles.models import VehiclesModel




class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = VehiclesModel
        fields = ('rodzaj', 'marka', 'model', 'VIN', 'nr_rej', 'rok_prod')


