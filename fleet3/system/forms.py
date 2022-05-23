
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=72)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
