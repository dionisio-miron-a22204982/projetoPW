"""PortfolioDio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from portfolio import views
app_name='portfolio'

urlpatterns = [
    path('', views.index_view),
    path('Menu/', views.menu_view, name="Menu"),
    path('Licenciatura/', views.Licenciatura_view, name="Licenciatura"),
    path('LEI/', views.LEI_view, name="LEI"),
    path('indexlab4/', views.index_lab4_view, name="indexlab4"),
    path('indexlab2/', views.index_lab2_view, name="indexlab2"),
    path('local/', views.local_view, name="local"),
    path('multimedia/', views.multimedia_view, name="multimedia"),
    path('info/', views.info_view, name="info"),
    path('quizz/', views.quizz_view, name="quizz"),
    path('html5-css/', views.html5_css_view, name="html5-css"),
    path('beach/', views.beach_view, name="beach"),
    path('parallax/', views.parallax_view, name="parallax"),
    path('animations/', views.animations_view, name="animations"),
    path('tourVeneza/', views.tourveneza_view, name="tourVeneza"),
    path('imagemReponsiva/', views.imagemReponsiva_view, name="imagemReponsiva"),
    path('calculadora/', views.calculadora_view, name="calculadora"),
    path('Main/', views.index_view, name="Main"),
    path('AboutMe/', views.about_me, name="AboutMe"),
]
