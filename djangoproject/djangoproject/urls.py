"""djangoproject URL Configuration

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
from pages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name="home"),
    path('cgpacalc/',cgpa_calc, name="cgpacalc"),
    path('sgpacalc/',sgpa_calc, name="sgpacalc"),
    path('sgpacalc/sgpasem7/',branch_select7, name="sgpasem7"),
    path('sgpacalc/sgpaphys/',sgpa_phys, name="sgpaphys"),
    path('sgpacalc/sgpachem/',sgpa_chem, name="sgpachem"),
    path('sgpacalc/sgpasem3/',sgpa_3, name="sgpa3"),
    path('sgpacalc/sgpasem4/',sgpa_4, name="sgpa4"),
    path('sgpacalc/sgpasem5/',sgpa_5, name="sgpa5"),
    path('sgpacalc/sgpasem6/',sgpa_6, name="sgpa6"),
    path('sgpacalc/sgpasem7/sgpa7cse/',sgpa_71, name="sgpa7"),
    path('sgpacalc/sgpasem7/sgpa7ece/',sgpa_72, name="sgpa7"),
    path('sgpacalc/sgpasem8/',sgpa_8, name="sgpa8"),
    path('contactus/', contact_us, name="conatct_us")
]
