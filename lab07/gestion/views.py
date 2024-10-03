from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Evento, RegistroEvento 
from .forms import LoginForm, EventoForm, RegistroEventoForm

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
                    request.session['user_id'] = usuario.id  
                    request.session['user_name'] = usuario.nombres
                    return redirect('menu')
                else:
                    messages.error(request, "Contraseña incorrecta.")
            except Usuario.DoesNotExist:
                messages.error(request, "El usuario no existe.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})  


def menu(request):
    return render(request, 'menu.html')

def listaEventos(request):
    eventos = Evento.objects.all()
    usuario_id = request.session['user_id']

    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        evento = get_object_or_404(Evento, id=evento_id)
        usuario = Usuario.objects.filter(id=usuario_id).first()

        if not RegistroEvento.objects.filter(evento=evento, usuario=usuario).exists():
            if not (usuario_id == evento.organizador_id):
                RegistroEvento.objects.create(evento=evento, usuario=usuario)
                messages.success(request, "Te has registrado en el evento exitosamente.")
            else:
                messages.error(request, "No puedes ingresar a tu mismo evento.")
        else:
            messages.error(request, "Ya estás registrado en este evento.")

        return redirect('listaEventos')

    return render(request, 'eventos/listarEventos.html', {'eventos': eventos, 'usuario_id': usuario_id})



def crearEvento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaEventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crearEvento.html', {'form': form})

def listaRegistros(request):
    return render(request, 'listarRegistros.html')

def actEvento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "El evento ha sido actualizado exitosamente.")
            return redirect('listaEventos')  
    else:
        form = EventoForm(instance=evento)

    return render(request, 'eventos/actualizarEvento.html', {'form': form, 'evento': evento})

def eliminarEvento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    evento.delete()
    messages.success(request, "El evento ha sido eliminado correctamente.")
    return redirect('listaEventos')

def misEventos(request):
    usuario_id = request.session['user_id']
    eventos = Evento.objects.filter(organizador_id=usuario_id)
    return render(request, 'eventos/misEventos.html', {'eventos': eventos})

def listarRegistros(request):
    registros = RegistroEvento.objects.all()
    return render(request, 'listarRegistros.html', {'registros': registros})