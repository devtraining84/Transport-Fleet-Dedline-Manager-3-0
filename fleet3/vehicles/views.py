from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from vehicles.models import VehiclesModel

# Create your views here.


class AddVehicleView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = VehiclesModel
    fields = '__all__'
    template_name = 'add_vehicle.html'
    success_url = '/add_vehicle/'
    success_message ='Dodano pojazd do bazy danych'
    

   


