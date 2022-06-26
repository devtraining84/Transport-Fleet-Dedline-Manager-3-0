from django.db import models
from vehicles.choice import *

# Create your models here.


class VehiclesModel(models.Model):
    rodzaj = models.CharField(choices=RODZAJE, max_length=64)
    marka = models.CharField(choices=MARKI, max_length=16)
    model = models.CharField(max_length=32, blank=True)
    VIN = models.CharField(max_length=17,  unique=True)
    nr_rej = models.CharField(max_length=8, unique=True, verbose_name='nr rej.')
    rok_prod = models.PositiveSmallIntegerField(choices=ROCZNIK[:-1], verbose_name='rok produkcji')
    truck = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marka} {self.model} nr rej. {self.nr_rej}"





class VehiclePermitsAndDedline(models.Model):
    pojazd = models.OneToOneField(VehiclesModel, on_delete=models.CASCADE, primary_key=True, related_name='vehicle')
    
    badanietechniczne_nazwa = models.CharField(max_length=32, default="Przegląd techniczy pojazdu")
    badanietechniczne_instytucja = models.CharField(default="Okręgowa Stacja Kontroli Pojazdów", max_length=40, null=True)
    badanietechniczne_wymagane = models.BooleanField(default=True)
    badanietechniczne_data_konc = models.DateField(null=True)
    
    tachograf_nazwa = models.CharField(max_length=60, default="Przegląd tachografu")
    tachograf_instytucja = models.CharField(default="Okręgowa Stacja Kontroli Pojazdów", max_length=40)
    tachograf_wymagane = models.BooleanField(default=False)
    trachograf_data_konc = models.DateField(blank=True, null=True)

    ADR_nazwa = models.CharField(max_length=32, default="Dopuszczenie do przewodu ADR")
    ADR_instytucja = models.CharField(default="TDT", max_length=40)
    ADR_wymagane = models.BooleanField(default=False)
    ADR_data_konc = models.DateField(blank=True, null=True)

    euro_norma = models.CharField(max_length=12, choices=EURO, default="nie dotyczy", null=True)
    euro_wymagane = models.BooleanField(default=False)

    FRC_nazwa = models.CharField(max_length=32, default="Badanie termiczne chłodni ATP/FRC")
    FRC_instytucja = models.CharField(default="Politechnika Poznańska, IMRiPS", max_length=40, null=True)
    FRC_wymagane = models.BooleanField(default=False)
    FRC_data_konc = models.DateField(blank=True, null=True)

    UDT_nazwa = models.CharField(max_length=60, default="Badanie dopuszczenia windy hydraulicznej lub HDS")
    UDT_instytucja = models.CharField(default="Urząd Dozoru Techniczego", max_length=40)
    UDT_wymagane = models.BooleanField(default=False)
    UDT_data_konc = models.DateField(blank=True, null=True)

    TDT_nazwa = models.CharField(max_length=64, default="Dozór zbiorników")
    TDT_instytucja = models.CharField(default="Transportowy Dozór Techniczny", max_length=40)
    TDT_wymagane = models.BooleanField(default=False)
    TDT_data_konc = models.DateField(blank=True, null=True)

    Ubezpieczeniakom_instytucja = models.CharField(default="Zakład Ubezpieczeń", max_length=72, null=True)
    Ubezpieczeniakom_OC = models.BooleanField(default=True)
    Ubezpieczeniakom_AC = models.BooleanField(default=False)
    Ubezpieczeniakom_NNW = models.BooleanField(default=False)
    Ubezpieczeniakom_data_konc = models.DateField(blank=True, null=True)
    Ubezpieczeniakom_nr_polisy = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.pojazd.nr_rej


