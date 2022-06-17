from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from vehicles.models import VehiclesModel
from vehicles.forms import SearchForm, BridgeForm, vehicle_form

# Create your views here.


class AddVehicleView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = VehiclesModel
    fields = '__all__'
    template_name = 'add_vehicle.html'
    success_url = '/add_vehicle/'
    success_message ='Dodano pojazd do bazy danych'




class SearchVehicleView(LoginRequiredMixin, View):
   
   def get(self, request):
        form = SearchForm(request.GET)
        form.is_valid()
        text = form.cleaned_data.get('text', '')
        result = VehiclesModel.objects.filter(
            Q(rodzaj__icontains=text)|
            Q(marka__icontains=text)|
            Q(model__icontains=text)|
            Q(VIN__icontains=text)|
            Q(nr_rej__icontains=text)
        )
        note = f"wyszukano {len(result)}"
        ctx ={
            'form': form,
            'pojazdy': result,
             'note': note,
             }
        return render(request, 'show_all.html', ctx)



class BridgeEditView(LoginRequiredMixin, View):
    
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_edit.html', {'form': form})
    
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            self_object = VehiclesModel.objects.filter(id=form.cleaned_data['id'])
            if len(self_object) > 0:
                return redirect(f'/vehicles/{self_object[0].id}/edit')
            else:
                info = 'Brak pojazdu o takim ID'
                return render(request, 'bridge_edit.html', {'form': form, 'info': info})




class EditVehicleView(LoginRequiredMixin, UpdateView):
    model = VehiclesModel
    fields = ['marka','model','nr_rej','rok_prod']
    template_name = 'edit_vehicle.html'
    success_url = '/search/'


class BridgeDelView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_del.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            obj = VehiclesModel.objects.filter(id=form.cleaned_data['id'])
            if obj.exists():
                return redirect(f'/delete/{obj[0].id}')
            else:
                info = 'Brak pojazdu o takim ID'
                return render(request, 'bridge_del.html', {'form': form, 'info': info})

    

class DeleteVehicleView(LoginRequiredMixin, View):
    def get(self, request, id):
        vehicle = VehiclesModel.objects.get(id=id)
        vehicle.delete()
        return redirect('/search/')




   


