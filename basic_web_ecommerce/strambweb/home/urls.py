from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),

]

'''

NoReverseMatch - En caso de este error, revise name='nombre de app' 
en ruta urls y que tenga coincidencia con views.

'''