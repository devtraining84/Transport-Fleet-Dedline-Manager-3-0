from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Start(TemplateView):
    template_name="start.html"

