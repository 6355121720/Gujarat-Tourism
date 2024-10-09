"""
URL configuration for GujaratTourism project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/',views.home,name='home'),
    path('aboutgujarat/',views.aboutgujarat,name='aboutgujarat'),
    path('experience1/',views.experience1,name='experience1'),
    path('experience2/',views.experience2,name='experience2'),
    path('experience3/',views.experience3,name='experience3'),
    path('experience4/',views.experience4,name='experience4'),
    path('experience5/',views.experience5,name='experience5'),
    path('experience6/',views.experience6,name='experience6'),
    path('experience7/',views.experience7,name='experience7'),
    path('experience8/',views.experience8,name='experience8'),
    path('experience9/',views.experience9,name='experience9'),
    path('experience10/',views.experience10,name='experience10'),
    path('experience11/',views.experience11,name='experience11'),
    path('experience12/',views.experience12,name='experience12'),
    path('experience13/',views.experience13,name='experience13'),
    path('recommendationsystem/',views.recommendation,name='recommendation'),
    path('hotel/',views.hotel,name='hotel'),
    path('shopping/',views.shopping,name='shopping'),
    path('weather/',views.weather,name='weather')

]

