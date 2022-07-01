from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from drivers.models import DriversModel


class AddDriverView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = DriversModel
    fields = '__all__'
    template_name = 'add_driver.html'
    success_url = '/adddriver/'
    success_message ='Dodano kierowce do bazy danych'
