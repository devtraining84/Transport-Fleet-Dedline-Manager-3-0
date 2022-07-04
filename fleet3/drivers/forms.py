from django import forms
from drivers.models import DriverCertificatesModel



class BookOfDriverForm(forms.ModelForm):
    class Meta:
        model = DriverCertificatesModel
        fields ='__all__'
