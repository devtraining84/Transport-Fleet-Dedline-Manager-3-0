from django import forms
from drivers.models import DriverCertificatesModel



class BookOfDriverForm(forms.ModelForm):
    class Meta:
        model = DriverCertificatesModel
        fields = ('B','CE','C','BE','C1','driver_licence_enddate','kwalifikacja_data_konc','ADR_data_konc','ADR_cat1','ADR_cat7')
        widgets = {
        'driver_licence_enddate': forms.DateInput(attrs={'type':'date'}),
        'kwalifikacja_data_konc': forms.DateInput(attrs={'type':'date'}),
        'ADR_data_konc': forms.DateInput(attrs={'type':'date'}),
         }
        
