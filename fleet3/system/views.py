from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from system.forms import LoginForm


class Start(TemplateView):
    template_name="start.html"

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('start/')
            else:
                text = 'Nieudane logowanie !'
        return render(
            request,
            'login.html',
            {'form': form, 'text': text}
        )

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class AlphaView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'alpha.html', {})