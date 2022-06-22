
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from vehicles.models import BtModel, VehiclesModel




class vehicle_form(forms.ModelForm):
    class Meta:
        model = VehiclesModel
        fields = ('rodzaj', 'marka', 'model', 'VIN', 'nr_rej', 'rok_prod', 'truck')




class SearchForm(forms.Form):
    text = forms.CharField(max_length=40, required=False, label="")        




class BridgeForm(forms.Form):
    id = forms.IntegerField(required=True, label="")




class BT_Form(forms.ModelForm):
    class Meta:
        model = BtModel
        fields = ['instytucja', 'wymagane', 'data_konc']
        widgets = {
        'data_konc': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
    }   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instytucja'].widget.attrs.update(size='50')
        self.fields['data_konc'].required = False
        self.fields['wymagane'].required = False
     