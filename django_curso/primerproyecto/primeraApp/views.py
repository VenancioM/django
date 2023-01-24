from django.shortcuts import render, HttpResponse, redirect
#Este es el controlador (vista) -> Acciones (metodos)

#MVC = Modelo Vista Controlador
# el controlador vendria siendo la vista en django
#MVT = Modelo Template Vista
# Create your views here.

layout = """
<h1>Sitio web con Django | Venancio Castillo</h1>
<hr/>
<ul>
    <li>
        <a href="/">Inicio</a>
    </li>
    <li>
       <a href="/holamundo">Pagina prueba</a>
    </li>
    <li>
       <a href="/pag">Contact</a>
    </li>
</ul>
<hr/>
"""

def index(request):

    html = """
         <h1>Inicio</h2>
         <p>Años hasta el 2050:</p>
         <ul>
    """
    year = 2019
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    
    html += "</ul>"
    return HttpResponse(layout+html)

def holamundo(request):
    return HttpResponse(layout+"Hola mundo en django")

def pag(request,nombre=""):
    return HttpResponse(layout+f"<h1>Nombre: {nombre}</h1>")

def redireccion(request, numero = 0):
    if numero == 1:
        return redirect('pag',nombre="Edgar")
    return HttpResponse(layout+"<h1>Mala suerte</h2>")