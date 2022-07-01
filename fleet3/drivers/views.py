from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from drivers.models import DriversModel
from vehicles.forms import BridgeForm




class AddDriverView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = DriversModel
    fields = '__all__'
    template_name = 'add_driver.html'
    success_url = '/adddriver/'
    success_message ='Dodano kierowce do bazy danych'




class UpdateDriverView(LoginRequiredMixin, UpdateView):
    model = DriversModel
    fields = '__all__'
    template_name = 'edit_driver.html'
    success_url = '/drivers/'




class DeleteDriverView(LoginRequiredMixin, View):
    def get(self, request, id):
        employee = DriversModel.objects.get(id=id)
        employee.delete()
        return redirect('/drivers/')




class ShowDriversView(LoginRequiredMixin, View):
    def get(self, request):
        drivers = DriversModel.objects.all()
        note = f"Kierowców w bazie {len(drivers)}"
        return render(request, 'show_drivers.html', {'drivers': drivers, 'note': note})




class EditDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_edit_driver.html', {'form':form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            object = DriversModel.objects.filter(id=form.cleaned_data['id'])
            if object.exists():
                return redirect(f'/editdriver/{object[0].id}')
            else:
                info = 'Brak kierowcy o takim ID'
                return render(request, 'bridge_edit_driver.html', {'form': form, 'info': info})





class DeleteDriverBridgeView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_del_driver.html', {'form': form})
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            if DriversModel.objects.filter(id=id).exists():
                return redirect(f'/deletedriver/{id}')
            else:
                info = "Brak kierowcy o podanym ID"
                return render(request, 'bridge_del_driver.html', {'form': form, 'info':info})
