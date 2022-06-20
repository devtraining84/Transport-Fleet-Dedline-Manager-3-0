
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from vehicles.models import VehiclesModel



class vehicle_form(forms.ModelForm):
    class Meta:
        model = VehiclesModel
        fields = ('rodzaj', 'marka', 'model', 'VIN', 'nr_rej', 'rok_prod', 'truck')


class SearchForm(forms.Form):
    text = forms.CharField(max_length=40, required=False, label="")        


class BridgeForm(forms.Form):
    id = forms.IntegerField(required=True, label="")