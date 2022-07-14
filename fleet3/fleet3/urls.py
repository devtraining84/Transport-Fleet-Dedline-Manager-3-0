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
from django.urls import path, re_path

from system.views import LoginView, LogoutView, AlphaView, StartView, HelpView, AboutView

from vehicles.views import AddAdrVehView, AddBtView, AddEuroView, AddFrcView, AddTachoView, AddTdtView, AddUdtView, AddUkView, AddVehicleView
from vehicles.views import BridgeDateView, DeleteVehicleView, SearchVehicleView, BridgeEditView, EditVehicleView, BridgeDelView, DeleteVehicleView
from vehicles.views import ShowVehicleView, BridgeDetailsVehicleView,  VehicleDetailsView, DedlineVehicleView

from drivers.views import BookOfDriverEditView, BridgeDatePersonView, DedlinePersonView, EditDriverBridgeView, SearchPersonView
from drivers.views import AddDriverView, BookOfDriverView, DeleteDriverBridgeView, DeleteDriverView, DetailsDriverBridgeView
from drivers.views import ShowDriversView, UpdateDriverView

#from drivers.views import *

urlpatterns = [
#system urls:    
    path('admin/', admin.site.urls),
    path('', StartView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="log-in"),
    path('login/start/', AlphaView.as_view(), name="front-site"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('help/', HelpView.as_view(), name='help'),
    path('about/',AboutView.as_view(), name='about'),
#vehicles urls:
    path('add_vehicle/', AddVehicleView.as_view(), name="add-vehicle"),  
    path('search/', SearchVehicleView.as_view(), name="search-vehicle"),
    path('edit/', BridgeEditView.as_view(), name="edit"),
    path('vehicles/<slug:pk>/edit/', EditVehicleView.as_view(), name="edit-view"),
    path('del/', BridgeDelView.as_view(), name="del"),
    path('delete/<int:id>/', DeleteVehicleView.as_view(), name="delete-vehicle"),
    path('vehiclelist/<int:select>/', ShowVehicleView.as_view(), name="list-of-vehicle"),
    path('details/', BridgeDetailsVehicleView.as_view(), name="detail"),
    path('details/<int:id>/', VehicleDetailsView.as_view(), name="vehicle-details"),
    #details for vehicle:
    path('addbt/<int:id>/', AddBtView.as_view(), name="add-bt"),
    path('addtacho/<int:id>', AddTachoView.as_view(), name="add-tacho"),
    path('adduk/<int:id>', AddUkView.as_view(), name="add-uk"),
    path('addadr/<int:id>', AddAdrVehView.as_view(), name="add-adr"),
    path('addudt/<int:id>', AddUdtView.as_view(), name="add-udt"),
    path('addfrc/<int:id>', AddFrcView.as_view(), name="add-frc"),
    path('addtdt/<int:id>', AddTdtView.as_view(), name="add-tdt"),
    path('addeuro/<int:id>', AddEuroView.as_view(), name="add-euro"),
    path('dedlineveh/', BridgeDateView.as_view(), name="dedline-veh-bridge"),
    re_path(r'^dedlinevehicle/(?P<date_string>\d{4}-\d{2}-\d{2})', DedlineVehicleView.as_view(),name="dedline-veh"),
#drivers urls:    
    path('drivers/', ShowDriversView.as_view(), name="show-drivers"),
    path('adddriver/', AddDriverView.as_view(), name="add-driver"),
    path('editdriver/<slug:pk>', UpdateDriverView.as_view(), name="edit-driver"),
    path('editdriver/', EditDriverBridgeView.as_view(), name="bridge-edit-driver"),
    path('deletedriver/<int:id>', DeleteDriverView.as_view(), name="delete-driver"),
    path('deletedriver/', DeleteDriverBridgeView.as_view(), name="del-bridge-driver"),
    path('searchperson/', SearchPersonView.as_view(), name="search-person"),
    path('detailsofdriver/<int:id>', BookOfDriverView.as_view(), name="driver-detail"),
    path('detailsofdriver/', DetailsDriverBridgeView.as_view(), name="detail-driver-bridge"),
    path('detailsofdriver/<int:id>/activform', BookOfDriverEditView.as_view(), name="driver-detail"),
    path('dedlineperson/', BridgeDatePersonView.as_view(), name="dedline-person-bridge"),
    re_path(r'^dedlineperson/(?P<date_string>\d{4}-\d{2}-\d{2})', DedlinePersonView.as_view(), name="dedline-person"),
]

