# Entrega1Galvan

Entrega intermedia del Proyecto final: Página web programada con Python y utilizando framework django

Documentos
Creación de proyecto Django (python -m django startproject ProyectoCoder)

Creación de app Django (python -m django startapp AppTrabajo)

Se descarga plantilla de bootstrap, la cual se modifica para el proyecto a presentar.

Se realiza herencias de padre a hijos renderizando las vistas a las plantillas según correspondan.

-------------------------------------------------------

Inicio
Nos encontramos con una primera vista general,diferentes redirecciones y al pie de la misma un buscador de Legajos de Gerentes.

Archivos py:
models.py
Aca encontramos el modelado de los datos que se utilizaron para el proyecto y base de datos.

forms.py
Aca encontramos los formularios necesarios para poder cargar datos en nuestra base de datos desde la página web.

views.py
Son las vistas creadas a partir de nuestros modelos y formularios para navegar por la web.

urls.py
Ubicación de todas las rutas utilizadas en este proyecto.

"Buscador Gerente por legajo":
Al pie de la página de inicio es factible buscar a los gerentes segun su legajo.
El programa consultará a la base de datos si existe; de ser así, devolerá el nombre buscado, de lo contrario lo informará.
