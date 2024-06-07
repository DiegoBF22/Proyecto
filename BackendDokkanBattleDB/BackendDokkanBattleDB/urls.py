"""
URL configuration for BackendDokkanBattleDB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from DokkanDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', views.devolverCartas),
    path('cards/<int:idCard>', views.devolverCartaPorId),
    path('categories/', views.devolverCategorias),
    path('categories/<int:idCategory>', views.devolverCategoriasPorId),
    path('banners/', views.devolverBanners),
    path('banners/<int:idBanner>', views.devolverBannerPorId),
    path('news/', views.devolverNews),
    path('news/<int:idNews>', views.devolverNewsPorId),
    path('events/', views.devolverEvents),
    path('events/<int:idEvent>', views.devolverEventPorId),
    path('eventType/', views.devolverEventType),
    path('eventType/<int:idEventType>', views.devolverEventTypePorId),
]
