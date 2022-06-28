from django import forms

class RegistroGerente(forms.Form):

    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField()
    fecha_ingreso = forms.DateField()

class RegistroVendedor(forms.Form):

    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField()
    fecha_ingreso = forms.DateField()

class RegistroExpedicionista(forms.Form):

    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField()
    fecha_ingreso = forms.DateField()        