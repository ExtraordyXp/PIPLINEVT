from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('vcount/',views.counting, name = 'passtocountingview'),
    path('pipline/gpsdata/',views.GPS, name = 'htmlgpsdataform'),
]