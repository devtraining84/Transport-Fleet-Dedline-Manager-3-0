from datetime import date
import datetime
#from socketserver import _RequestType
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from datetime import date, datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from vehicles.models import VehiclesModel, VehiclePermitsAndDedlinesModel
from vehicles.forms import ADR_Form, BT_Form, BridgeDateForm, Euro_Form, FRC_Form, SearchForm, BridgeForm, EditVehicleComplexForm, TDT_Form, Tacho_Form, UDT_Form, UK_Form

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
            'vehicles': result,
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
    success_url = '/vehiclelist/0/'




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
        return redirect('/vehiclelist/0/')




class ShowVehicleView(LoginRequiredMixin, View):
    def get(self, request, select):
        if select == 0:
            vehicles = VehiclesModel.objects.all()
            note = f"(wszystkie vehicles). Pojazdów w bazie {len(vehicles)}"
        elif select == 1:
            vehicles = VehiclesModel.objects.filter(truck=True)
            note = f"(tylko samochody ciężarowe i ciągniki siodłowe).Pojazdów w bazie {len(vehicles)}"
        elif select == 2:
            vehicles = VehiclesModel.objects.filter(truck=False)
            note = f"(tylko przyczepy i naczepy).Pojazdów w bazie {len(vehicles)}"
        return render(request, 'show_all.html', {'vehicles': vehicles, 'note': note})


   

class BridgeDetailsVehicleView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeForm()
        return render(request, 'bridge_book.html', {'form': form})
    
    def post(self, request):
        form = BridgeForm(request.POST)
        if form.is_valid():
            obj = VehiclesModel.objects.filter(id=form.cleaned_data['id'])
            if obj.exists():
                return redirect(f'/details/{obj[0].id}')
            else:
                info = 'Brak pojazdu o takim ID'
                return render(request, 'bridge_del.html', {'form': form, 'info': info})    





class BridgeDateView(LoginRequiredMixin, View):
    def get(self, request):
        form = BridgeDateForm()
        return render(request, 'dedline_bridge.html', {'form': form})
    def post(self, request):
        form = BridgeDateForm(request.POST)
        if form.is_valid():
            date2 = form.cleaned_data['date2']
            return redirect(f'/dedlinevehicle/{date2}')
        else:
            info = "Nieprawidłowe dane"
            return render(request, 'dedline_bridge.html', {'form': form, 'info': info})





class VehicleDetailsView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.filter(id=id)
        today = date.today()
        return render(request, 'detail.html', {'unit': unit,'today': today})




class VehicleDetailsFormView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.filter(id=id)
        today = date.today()
        form = EditVehicleComplexForm
        return render(request, 'detail.html', {'unit': unit,'today': today, 'form': form})        




class AddBtView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit=VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = BT_Form(instance=bt_unit)
        else:
            form = BT_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'add_BT.html', ctx)
   
    def post(self,request, id):
        unit = VehiclesModel.objects.get(id=id)
        object, created = VehiclePermitsAndDedlinesModel.objects.update_or_create(pojazd=unit)
        form = BT_Form(request.POST, instance=object)
        if form.is_valid():
                form.save()
                return redirect(f'/details/{id}')





class AddTachoView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit = VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = Tacho_Form(instance=bt_unit)
        else:
            form = Tacho_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'add_tacho.html', ctx)
    def post(self,request, id):
        unit = VehiclesModel.objects.get(id=id)
        object, created = VehiclePermitsAndDedlinesModel.objects.get_or_create(pojazd=unit)
        form = Tacho_Form(request.POST, instance=object)
        if form.is_valid():
                form.save()
                return redirect(f'/details/{id}')


        

class AddUkView(LoginRequiredMixin, View):
   def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        form = UK_Form()
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit = VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = UK_Form(instance=bt_unit)
        ctx = {'unit': unit, 'form': form}
        return render(request, 'adduk.html', ctx)
   def post(self,request, id):
       unit = VehiclesModel.objects.get(id=id)
       object, created = VehiclePermitsAndDedlinesModel.objects.get_or_create(pojazd=unit)
       form = UK_Form(request.POST, instance=object)
       if form.is_valid():
           form.save()
           return redirect(f'/details/{id}')
       



class AddAdrVehView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit = VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = ADR_Form(instance=bt_unit)
        else:
            form = ADR_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addadr.html', ctx)
    def post(self,request, id):
        unit = VehiclesModel.objects.get(id=id)
        object, created = VehiclePermitsAndDedlinesModel.objects.get_or_create(pojazd=unit)
        form = ADR_Form(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/details/{id}')




class AddUdtView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit = VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = UDT_Form(instance=bt_unit)
        else:
            form = UDT_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addudt.html', ctx)
    def post(self,request, id):
        unit = VehiclesModel.objects.get(id=id)
        object, created = VehiclePermitsAndDedlinesModel.objects.get_or_create(pojazd=unit)
        form = UDT_Form(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/details/{id}')




class AddFrcView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit = VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = FRC_Form(instance=bt_unit)
        else:
            form = FRC_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addfrc.html', ctx)
    def post(self,request, id):
        unit = VehiclesModel.objects.get(id=id)
        object, created = VehiclePermitsAndDedlinesModel.objects.get_or_create(pojazd=unit)
        form = FRC_Form(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/details/{id}')




class AddTdtView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit = VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = TDT_Form(instance=bt_unit)
        else:
            form = TDT_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addtdt.html', ctx)
    def post(self,request, id):
        unit = VehiclesModel.objects.get(id=id)
        form = TDT_Form(request.POST)
        object, created = VehiclePermitsAndDedlinesModel.objects.get_or_create(pojazd=unit)
        form = TDT_Form(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/details/{id}')





class AddEuroView(LoginRequiredMixin, View):
    def get(self, request, id):
        unit = VehiclesModel.objects.get(id=id)
        if VehiclePermitsAndDedlinesModel.objects.filter(pojazd=unit).exists():
            bt_unit = VehiclePermitsAndDedlinesModel.objects.get(pojazd=unit)
            form = Euro_Form(instance=bt_unit)
        else:
            form = Euro_Form()
        ctx = {'unit': unit, 'form': form}
        return render(request, 'addeuro.html', ctx)
    def post(self,request, id):
        unit = VehiclesModel.objects.get(id=id)
        form = Euro_Form(request.POST)
        object, created = VehiclePermitsAndDedlinesModel.objects.get_or_create(pojazd=unit)
        form = Euro_Form(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect(f'/details/{id}')




class DedlineVehicleView(LoginRequiredMixin, View):
    def get(self, request, date_string):
        dedline = datetime.strptime(date_string, "%Y-%m-%d")
        dedline = datetime.date(dedline)
        vehicles = VehiclesModel.objects.filter(
            Q(details__badanietechniczne_data_konc__lte=dedline)|
            Q(details__tachograf_data_konc__lte=dedline)|
            Q(details__ADR_data_konc__lte=dedline)|
            Q(details__TDT_data_konc__lte=dedline)|
            Q(details__UDT_data_konc__lte=dedline)|
            Q(details__Ubezpieczeniakom_data_konc__lte=dedline)|
            Q(details__FRC_data_konc__lt=dedline)
        )
        note = f"(Pojazdy z końcem terminu). Liczba pojazdów ze zbliżającym się terminem: {len(vehicles)}"
        return render(request, 'show_all.html', {'vehicles': vehicles, 'note': note})





