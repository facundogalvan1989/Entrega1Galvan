from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from AppTrabajo.forms import RegistroExpedicionista, RegistroGerente, RegistroVendedor
from AppTrabajo.models import *

# Create your views here.

def inicio(request):

    return render(request, "Apptrabajo/inicio.html")

def gerente(request):

  return render(request, "AppTrabajo/gerente.html", {'gerentes': Gerente.objects.all()})


def registroGerente(request):

    if request.method == 'POST':

            registro = RegistroGerente(request.POST)

            print(registro)

            if registro.is_valid: 

                  informacion = registro.cleaned_data

                  gerente = Gerente (nombre=informacion['nombre'], legajo=informacion['legajo'],
                   fecha_ingreso=informacion['fecha_ingreso']) 

                  gerente.save()

                  return render(request, "AppTrabajo/inicio.html") 

    else:
        
        registro = RegistroGerente() 

    return render(request, "AppTrabajo/registroGerente.html", {"registro": registro})
  

def vendedor(request):

    return render(request, "AppTrabajo/vendedor.html", {'vendedores': Vendedor.objects.all()})

def registroVendedor(request):

    if request.method == 'POST':

            registro = RegistroVendedor(request.POST) 

            print(registro)

            if registro.is_valid:  

                  informacion = registro.cleaned_data

                  vendedor = Vendedor (nombre=informacion['nombre'], legajo=informacion['legajo'],
                   fecha_ingreso=informacion['fecha_ingreso']) 

                  vendedor.save()

                  return render(request, "AppTrabajo/inicio.html") 

    else:
        
        registro = RegistroVendedor()

    return render(request, "AppTrabajo/registroVendedor.html", {"registro": registro})    

def expedicionista(request):

    return render(request, "AppTrabajo/expedicionista.html", {'expedicionistas': Expedicionista.objects.all()})

def registroExpedicionista(request):

    if request.method == 'POST':

            registro = RegistroExpedicionista(request.POST) 

            print(registro)

            if registro.is_valid: 

                  informacion = registro.cleaned_data

                  expedicionista = Expedicionista (nombre=informacion['nombre'], legajo=informacion['legajo'],
                   fecha_ingreso=informacion['fecha_ingreso']) 

                  expedicionista.save()

                  return render(request, "AppTrabajo/inicio.html") #Vuelvo al inicio o a donde quieran

    else:
        
        registro = RegistroExpedicionista() #Formulario vacio para construir el html

    return render(request, "AppTrabajo/registroExpedicionista.html", {"registro": registro})

"""def buscar(request):

      if  request.GET["legajo"]:

            legajo = request.GET['legajo']
            print(legajo)
            gerente = Gerente.objects.filter(legajo__icontains=legajo)
            print(gerente)

            return render(request, "AppTrabajo/inicio.html", {"gerente":gerente, "legajo":legajo})

      else:
        respuesta = "Sin datos"
        
        return render(request, "AppTrabajo/inicio.html", {"respuesta": respuesta})
        """

def busquedaNombre(request):

    return render(request, "AppTrabajo/busquedaNombre.html")

def buscar(request):

    if request.GET["legajo"]:

        legajo = request.GET["legajo"]
        gerente = Gerente.objects.filter(legajo__icontains=legajo)
        if gerente:
            return render(request, "AppTrabajo/busquedaNombre.html", {"gerente":gerente, "legajo":legajo})
        else:
            respuesta = "No existe este legajo en nuestra base de datos"
            return render(request, "AppTrabajo/busquedaNombre.html", {"respuesta": respuesta})
        #vendedor = Vendedor.objects.filter(legajo__icontains=legajo)   

        
    
    else:
        respuesta = "No se encuentra dicho legajo"
        return render(request, "AppTrabajo/busquedaNombre.html", {"respuesta": respuesta})
