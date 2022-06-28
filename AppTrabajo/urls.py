from django.urls import path
from AppTrabajo import views 

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('gerente', views.gerente, name="Gerente"),
    path('vendedor', views.vendedor, name="Vendedor"),
    path('expedicionista', views.expedicionista, name="Expedicionista"),
    path('registroGerente', views.registroGerente, name="RegistroGerente"),
    path('registroVendedor', views.registroVendedor, name="RegistroVendedor"),
    path('registroExpedicionista', views.registroExpedicionista, name="RegistroExpedicionista"),
    path('busquedaNombre', views.busquedaNombre, name="BusquedaNombre"),
    path('buscar/', views.buscar),
    ]