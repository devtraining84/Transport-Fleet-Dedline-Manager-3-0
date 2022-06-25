from django.db import models
from django.core.exceptions import ValidationError
from vehicles.choice import *
from django.core.exceptions import ValidationError



# Create your models here.
def VIN_validator(value):
    if len(value) != 17:
        raise ValidationError('VIN 17 znaków !')


def VIN_unique(value):
    data = VehiclesModel.objects.all()
    vins = []
    for i in data:
        vins.append(i.VIN)
    if value in vins:
        raise ValidationError('VIN juz istnieje w bazie !')


def REJ_validator(value):
    if len(value) < 3:
        raise ValidationError('Za mało znaków !')


def REJ_unique(value):
    data = VehiclesModel.objects.all()
    nrs = []
    for i in data:
        nrs.append(i.VIN)
    if value in nrs:
        raise ValidationError('Nr juz istnieje w bazie !')



class VehiclesModel(models.Model):
    rodzaj = models.CharField(choices=RODZAJE, max_length=64)
    marka = models.CharField(choices=MARKI, max_length=16)
    model = models.CharField(max_length=32, blank=True)
    VIN = models.CharField(max_length=17,  unique=True, validators=[VIN_validator, VIN_unique])
    nr_rej = models.CharField(max_length=8, unique=True, verbose_name='nr rej.', validators=[REJ_validator, REJ_unique])
    rok_prod = models.PositiveSmallIntegerField(choices=ROCZNIK[:-1], verbose_name='rok produkcji')
    truck = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marka} {self.model} nr rej. {self.nr_rej}"




class BtModel(models.Model):
    nazwa = models.CharField(max_length=32, default="Przegląd techniczy pojazdu")
    instytucja = models.CharField(default="Okręgowa Stacja Kontroli Pojazdów", max_length=40, null=True)
    wymagane = models.BooleanField(default=True)
    data_konc = models.DateField(null=True)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True, related_name='przegladtech')
    def __str__(self):
        return self.pojazd.nr_rej




class TachoModel(models.Model):
    nazwa = models.CharField(max_length=60, default="Przegląd tachografu")
    instytucja = models.CharField(default="Okręgowa Stacja Kontroli Pojazdów", max_length=40)
    wymagane = models.BooleanField(default=False)
    data_konc = models.DateField(blank=True, null=True)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, related_name='przegladtacho')
    def __str__(self):
        return self.pojazd.nr_rej




class AdrModel(models.Model):
    nazwa = models.CharField(max_length=32, default="Dopuszczenie do przewodu ADR")
    instytucja = models.CharField(default="TDT", max_length=40)
    wymagane = models.BooleanField(default=False)
    data_konc = models.DateField(blank=True, null=True)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True, related_name='przegladadr')
    def __str__(self):
        return self.pojazd.nr_rej   




class NormaCzystosciSpalin(models.Model):
    norma = models.CharField(max_length=12, choices=EURO, default="nie dotyczy", null=True)
    wymagane = models.BooleanField(default=False)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True , related_name='normaeuro')




class FrcModel(models.Model):
    nazwa = models.CharField(max_length=32, default="Badanie termiczne chłodni ATP/FRC")
    instytucja = models.CharField(default="Politechnika Poznańska, IMRiPS", max_length=40, null=True)
    wymagane = models.BooleanField(default=False)
    data_konc = models.DateField(blank=True, null=True)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True, related_name='przegladfrc')
    def __str__(self):
        return self.pojazd.nr_rej                 




class UdtModel(models.Model):
    nazwa = models.CharField(max_length=60, default="Badanie dopuszczenia windy hydraulicznej lub HDS")
    instytucja = models.CharField(default="Urząd Dozoru Techniczego", max_length=40)
    wymagane = models.BooleanField(default=False)
    data_konc = models.DateField(blank=True, null=True)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True, related_name='przegladudt')
    def __str__(self):
        return self.pojazd.nr_rej




class TDT(models.Model):
    nazwa = models.CharField(max_length=64, default="Dozór zbiorników")
    instytucja = models.CharField(default="Transportowy Dozór Techniczny", max_length=40)
    wymagane = models.BooleanField(default=False)
    data_konc = models.DateField(blank=True, null=True)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True, related_name='przegladtdt')
    def __str__(self):
        return self.pojazd.nr_rej




class UkoModel(models.Model):
    instytucja = models.CharField(default="Zakład Ubezpieczeń", max_length=72, null=True)
    OC = models.BooleanField(default=True)
    AC = models.BooleanField(default=False)
    NNW = models.BooleanField(default=False)
    data_konc = models.DateField(blank=True, null=True)
    nr_polisy = models.CharField(max_length=32, null=True)
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True, related_name='komunikacyjne')







