from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from vehicles.models import VehiclesModel
from vehicles.forms import AddVehicleForm
# Create your views here.



class AddVehicleView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddVehicleForm()
        ctx = {
            'form': form,
                   }
        return render(request, 'add_vehicle.html', ctx)
    def post(self, request):
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            info = 'Dodano pojazd do bazy danych'
            new_vehicle = VehiclesModel.objects.create(**form.cleaned_data)
            return render(request, 'add_vehicle.html', {'form':form, 'info':info})
        else:
            info = 'Niepoprawne dane !'
            return render(request, 'add_vehicle.html', {'form': form, 'info': info})




