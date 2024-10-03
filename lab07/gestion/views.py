from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Evento, RegistroEvento  # Asegúrate de importar tu modelo Usuario
from .forms import LoginForm, EventoForm, RegistroEventoForm   # Importa tu formulario de login

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            contraseña = form.cleaned_data['contraseña']
            
            try:
                usuario = Usuario.objects.get(nombres=nombres)  
                if usuario.contraseña == contraseña:  
                    messages.success(request, "Inicio de sesión exitoso.")
                    return redirect('menu')  # Redirige a la vista 'menu'
                else:
                    messages.error(request, "Contraseña incorrecta." )
            except Usuario.DoesNotExist:
                messages.error(request, "El usuario no existe.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})  

def menu(request):
    return render(request, 'menu.html')

def listaEventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listarEventos.html', {'eventos': eventos})

def crearEvento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaEventos')  # Redirige a la lista de eventos después de guardar
    else:
        form = EventoForm()
    return render(request, 'eventos/crearEvento.html', {'form': form})

def listaRegistros(request):
    return render(request, 'listarRegistros.html')