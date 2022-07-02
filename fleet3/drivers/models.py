from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def PESEL_walidator(value):
    if len(value) != 11:
        raise ValidationError('PESEL 11 znaków !')




class DriversModel(models.Model):
    PESEL = models.CharField(max_length=11, unique=True, validators=[PESEL_walidator])
    firstname = models.CharField(max_length=32, verbose_name="imie")
    lastname = models.CharField(max_length=32, verbose_name="nazwisko")
    



class DriverCertificatesModel(models.Model):
    driver = models.OneToOneField(DriversModel, on_delete=models.CASCADE, primary_key=True, related_name="certyficate")

    driver_licence_enddate = models.DateField(verbose_name="Prawo Jazdy data koncowa")
    B = models.BooleanField(default=True)
    CE = models.BooleanField(default=True)
    C = models.BooleanField(default=True)
    BE = models.BooleanField(default=False)
    C1 = models.BooleanField(default=False)
    kwalifikacja_data_konc = models.DateField(verbose_name="Swiadectwo kwal. data koncowa")
    ADR_data_konc = models.DateField(verbose_name="ADR data koncowa")
    ADR_cat1 = models.BooleanField(default=False, verbose_name="kat 1")
    ADR_cat7 = models.BooleanField(default=False, verbose_name="kat 7")







   

   