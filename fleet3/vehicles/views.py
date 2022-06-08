from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from vehicles.models import VehiclesModel
from vehicles.forms import SearchForm

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

    

   


