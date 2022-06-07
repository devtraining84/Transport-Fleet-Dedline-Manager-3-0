from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from vehicles.models import PojazdyModel
# Create your models here.


def VIN_validator(value):
    if len(value) != 17:
        raise ValidationError('VIN 17 znaków !')

def VIN_unique(value):
    data = PojazdyModel.objects.all()
    vins = []
    for i in data:
        vins.append(i.VIN)
    if value in vins:
        raise ValidationError('VIN juz istnieje w bazie !')
def REJ_validator(value):
    if len(value) < 3:
        raise ValidationError('Za mało znaków !')
def REJ_unique(value):
    data = PojazdyModel.objects.all()
    nrs = []
    for i in data:
        nrs.append(i.VIN)
    if value in nrs:
        raise ValidationError('Nr juz istnieje w bazie !')