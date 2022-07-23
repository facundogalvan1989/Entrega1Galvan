from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from AppTrabajo.forms import RegistroExpedicionista, RegistroGerente, RegistroVendedor, UserRegisterForm, UserEditForm
from AppTrabajo.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    #avatares = Avatar.objects.filter(user=request.user.id)  
    return render(request, "AppTrabajo/inicio.html")#, {"url": avatares[1].imagen.url})

@login_required
def gerente(request):

  return render(request, "AppTrabajo/gerente.html", {'gerentes': Gerente.objects.all()})

@login_required
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

@login_required  
def leerGerente(request):

    gerente = Gerente.objects.all()
    contexto = {"Gerente": gerente}

    return render(request, "AppTrabajo/leerGerente.html", contexto)

@login_required
def eliminarGerente(request, gerente_legajo):

    gerente = Gerente.objects.get(legajo = gerente_legajo)
    gerente.delete()

    gerentes = Gerente.objects.all()    
    contexto = {"Gerentes": gerentes}

    return render(request, "AppTrabajo/leerGerente.html", contexto)

@login_required
def editarGerente(request, gerente_legajo):

    gerente = Gerente.objects.get(legajo = gerente_legajo)

    if request.method == 'POST':

        registro = RegistroGerente(request.POST)

        print(registro)

        if registro.is_valid:

            informacion = registro.cleaned_data

            gerente.nombre = informacion['nombre']
            gerente.legajo = informacion['legajo']
            gerente.fecha_ingreso = informacion['fecha_ingreso']

            gerente.save()

            return render(request, "AppTrabajo/leerGerente.html")
    
    else:

        registro = RegistroGerente(initial={'nombre': gerente.nombre, 'legajo':gerente.legajo, 'fecha_ingreso': gerente.fecha_ingreso})
    
    return render(request, "AppTrabajo/editarGerente.html", {"registro": registro, "gerente_legajo": gerente_legajo})

def vendedor(request):

    return render(request, "AppTrabajo/vendedor.html", {'vendedores': Vendedor.objects.all()})

@login_required
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

def leerVendedor(request):

    vendedor = Vendedor.objects.all()
    contexto = {"Vendedor": vendedor}

    return render(request, "AppTrabajo/leerVendedor.html", contexto)

@login_required
def eliminarVendedor(request, vendedor_legajo):

    vendedor = Vendedor.objects.get(legajo = vendedor_legajo)
    vendedor.delete()

    vendedores = Vendedor.objects.all()    
    contexto = {"Vendedores": vendedor}

    return render(request, "AppTrabajo/leerVendedor.html", contexto)

@login_required
def editarVendedor(request, vendedor_legajo):

    vendedor = Vendedor.objects.get(legajo = vendedor_legajo)

    if request.method == 'POST':

        registro = RegistroVendedor(request.POST)

        print(registro)

        if registro.is_valid:

            informacion = registro.cleaned_data

            vendedor.nombre = informacion['nombre']
            vendedor.legajo = informacion['legajo']
            vendedor.fecha_ingreso = informacion['fecha_ingreso']

            vendedor.save()

            return render(request, "AppTrabajo/vendedor.html")
    
    else:

        registro = RegistroVendedor(initial={'nombre': vendedor.nombre, 'legajo':vendedor.legajo, 'fecha_ingreso': vendedor.fecha_ingreso})
    
    return render(request, "AppTrabajo/editarVendedor.html", {"registro": registro, "vendedor_legajo": vendedor_legajo})        

def expedicionista(request):

    return render(request, "AppTrabajo/expedicionista.html", {'expedicionistas': Expedicionista.objects.all()})

@login_required
def registroExpedicionista(request):

    if request.method == 'POST':

            registro = RegistroExpedicionista(request.POST) 

            print(registro)

            if registro.is_valid: 

                  informacion = registro.cleaned_data

                  expedicionista = Expedicionista (nombre=informacion['nombre'], legajo=informacion['legajo'],
                   fecha_ingreso=informacion['fecha_ingreso']) 

                  expedicionista.save()

                  return render(request, "AppTrabajo/inicio.html")
    else:
        
        registro = RegistroExpedicionista() #Formulario vacio para construir el html

    return render(request, "AppTrabajo/registroExpedicionista.html", {"registro": registro})

def leerExpedicionista(request):

    expedicionista = Expedicionista.objects.all()
    contexto = {"Expedicionista": expedicionista}

    return render(request, "AppTrabajo/leerExpedicionista.html", contexto)

@login_required
def eliminarExpedicionista(request, expedicionista_legajo):

    expedicionista = Expedicionista.objects.get(legajo = expedicionista_legajo)
    expedicionista.delete()

    expedicionistas = Expedicionista.objects.all()    
    contexto = {"Expedicionista": expedicionistas}

    return render(request, "AppTrabajo/leerExpedicionista.html", contexto)

@login_required
def editarExpedicionista(request, expedicionista_legajo):

    expedicionista = Expedicionista.objects.get(legajo = expedicionista_legajo)

    if request.method == 'POST':

        registro = RegistroExpedicionista(request.POST)

        print(registro)

        if registro.is_valid:

            informacion = registro.cleaned_data

            expedicionista.nombre = informacion['nombre']
            expedicionista.legajo = informacion['legajo']
            expedicionista.fecha_ingreso = informacion['fecha_ingreso']

            expedicionista.save()

            return render(request, "AppTrabajo/leerExpedicionista.html")
    
    else:

        registro = RegistroExpedicionista(initial={'nombre': expedicionista.nombre, 'legajo':expedicionista.legajo, 'fecha_ingreso': expedicionista.fecha_ingreso})
    
    return render(request, "AppTrabajo/editarExpedicionista.html", {"registro": registro, "expedicionista_legajo": expedicionista_legajo})

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
    
    else:
        respuesta = "No se encuentra dicho legajo"
        return render(request, "AppTrabajo/busquedaNombre.html", {"respuesta": respuesta})

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username= usuario, password= contra)

            if user is not None:
                login(request, user)

                return render(request, "AppTrabajo/inicio.html", {"mensaje": f"Bienvenido {usuario}"})

            else:

                return render(request, "AppTrabajo/inicio.html", {"mensaje": "Error, datos incorretos"})

        else:

            return render(request, "AppTrabajo/inicio.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppTrabajo/login.html", {"form": form})      

def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "AppTrabajo/inicio.html", {"mensaje": "Usuario creado."})

      else:
        
        form = UserRegisterForm()
        
        return render(request, "AppTrabajo/register.html", {"form": form}) 

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
            registro = UserEditForm(request.POST)
            if registro.is_valid():
                  informacion = registro.cleaned_data
                  
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppTrabajo/inicio.html")

    else:
        registro = UserEditForm(initial={'email':usuario.email})
      
    return render(request, "AppTrabajo/editarPerfil.html", {"Registro": registro, "usuario": usuario})    

def pages(request):

    return render(request, "AppTrabajo/pages.html")                