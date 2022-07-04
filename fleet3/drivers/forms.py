from django import forms
from drivers.models import DriverCertificatesModel



class EditVehicleComplexForm(forms.ModelForm):
    class Meta:
        model = DriverCertificatesModel
        fields ='__all__'
