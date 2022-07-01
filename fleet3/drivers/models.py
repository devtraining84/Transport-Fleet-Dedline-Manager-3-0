from django.db import models

# Create your models here.
class DriversModel(models.Model):
    PESEL = models.CharField(max_length=11, unique=True)
    firstname = models.CharField(max_length=32, verbose_name="imie")
    lastname = models.CharField(max_length=32, verbose_name="nazwisko")
    hiring_date = models.DateField(null=True, verbose_name="data zatrudnienia")


#  class PrawoJazdyModel(models.Model):
#     driver = models.OneToOneField(DriversModel, on_delete=models.CASCADE, primary_key=True, related_name="prawojazdy")
#     data_waznosci = models.DateField()
#     B = models.BooleanField(default=True)
#     CE = models.BooleanField(default=True)
#     C = models.BooleanField(default=True)
#     BE = models.BooleanField(default=False)
#     C1 = models.BooleanField(default=False)




# class Kwalifikacja(models.Model):
#     kierowca = models.OneToOneField(Kierowcy, on_delete=models.CASCADE, primary_key=True, related_name="kwalifikacja")
#     data_waznosci = models.DateField()

# class ADRdriver(models.Model):
#     kierowca = models.OneToOneField(Kierowcy, on_delete=models.CASCADE, primary_key=True, related_name="adr")
#     data_waznosci = models.DateField()
#     kat1 = models.BooleanField(default=False)
#     kat7 = models.BooleanField(default=False)


   