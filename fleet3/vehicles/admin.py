from django.contrib import admin
from vehicles.models import VehiclePermitsAndDedlinesModel, VehiclesModel
# Register your models here.




@admin.register(VehiclesModel)
class VehiclesModel(admin.ModelAdmin):
    pass





@admin.register(VehiclePermitsAndDedlinesModel)
class VehiclePermitsAndDedlinesModel(admin.ModelAdmin):
    pass




