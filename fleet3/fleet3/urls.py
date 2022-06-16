"""fleet3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from system.views import Start, LoginView, LogoutView, AlphaView

from vehicles.views import AddVehicleView, SearchVehicleView, BridgeEditView, EditVehicleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Start.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="log-in"),
    path('login/start/', AlphaView.as_view(), name="front-site"),
    path('logout/', LogoutView.as_view(), name="logout"),
#vehicles urls:
    path('add_vehicle/', AddVehicleView.as_view(), name="add-vehicle"),  
    path('search/', SearchVehicleView.as_view(), name="search-vehicle"),
    path('edit/', BridgeEditView.as_view(), name="edit"),
    path('vehicles/<slug:pk>/edit/', EditVehicleView.as_view(), name="edit-view"),
    
]
