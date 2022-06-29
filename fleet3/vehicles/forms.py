
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from vehicles.models import VehiclesModel, VehiclePermitsAndDedlinesModel



class vehicle_form(forms.ModelForm):
    class Meta:
        model = VehiclesModel
        fields = ('rodzaj', 'marka', 'model', 'VIN', 'nr_rej', 'rok_prod', 'truck')




class SearchForm(forms.Form):
    text = forms.CharField(max_length=40, required=False, label="")        




class BridgeForm(forms.Form):
    id = forms.IntegerField(required=True, label="")




class EditVehicleComplexForm(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields ='__all__'





class BT_Form(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields = ['badanietechniczne_instytucja', 'badanietechniczne_wymagane', 'badanietechniczne_data_konc']
        widgets = {
        'data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
    }   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['badanietechniczne_instytucja'].widget.attrs.update(size='50')
        self.fields['badanietechniczne_data_konc'].required = False
        self.fields['badanietechniczne_wymagane'].required = False




class FRC_Form(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields = ['FRC_instytucja', 'FRC_wymagane', 'FRC_data_konc']
        widgets = {
        'FRC_data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        } 
   




class Tacho_Form(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields = ['tachograf_instytucja', 'tachograf_wymagane', 'tachograf_data_konc']
        widgets = {
        'tachograf_data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }   
     



class UK_Form(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields =[
            'Ubezpieczeniakom_instytucja', 'Ubezpieczeniakom_data_konc', 'Ubezpieczeniakom_nr_polisy',
            'Ubezpieczeniakom_OC', 'Ubezpieczeniakom_AC', 'Ubezpieczeniakom_NNW'
            ]
        widgets = {
        'Ubezpieczeniakom_data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }  




class ADR_Form(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields = ['ADR_instytucja', 'ADR_wymagane', 'ADR_data_konc']
        widgets = {
        'ADR_data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }  




class UDT_Form(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields = ['UDT_instytucja', 'UDT_wymagane', 'UDT_data_konc']
        widgets = {
        'UDT_data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }  





class TDT_Form(forms.ModelForm):
    class Meta:
        model = VehiclePermitsAndDedlinesModel
        fields = ['TDT_instytucja', 'TDT_wymagane', 'TDT_data_konc']
        widgets = {
        'TDT_data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }  



