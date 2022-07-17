from django.contrib import admin
from drivers.models import DriversModel, DriverCertificatesModel
# Register your models here.




@admin.register(DriversModel)
class DriversModel(admin.ModelAdmin):
    pass




@admin.register(DriverCertificatesModel)
class DriverCertificatesModel(admin.ModelAdmin):
    pass
