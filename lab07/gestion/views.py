from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Evento, RegistroEvento 
from .forms import LoginForm, EventoForm, UpdateEventoForm

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

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_name']
        messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('index')

def menu(request):
    return render(request, 'menu.html')

def listaEventos(request):
    usuario_id = request.session['user_id']
    eventos = Evento.objects.exclude(organizador = usuario_id).order_by('fecha')

    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        evento = get_object_or_404(Evento, id=evento_id)

        usuario = Usuario.objects.filter(id=usuario_id).first()

        if not RegistroEvento.objects.filter(evento=evento, usuario=usuario).exists():
            RegistroEvento.objects.create(evento=evento, usuario=usuario)
            messages.success(request, "Te has registrado en el evento exitosamente.")
        else:
            messages.error(request, "Ya estás registrado en este evento.")

        return redirect('listaEventos')

    return render(request, 'eventos/listarEventos.html', {'eventos': eventos, 'usuario_id': usuario_id})



def crearEvento(request):
    usuario = Usuario.objects.filter(id=request.session.get('user_id')).first()

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.organizador = usuario
            evento.save()  
            return redirect('listaEventos')
    else:
        form = EventoForm()
    
    return render(request, 'eventos/crearEvento.html', {'form': form})

def listaRegistros(request):
    return render(request, 'listarRegistros.html')

def actEvento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        form = UpdateEventoForm(request.POST, instance=evento)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.save()
            return redirect('listaEventos')
    else:
        form = UpdateEventoForm(instance=evento)
    
    return render(request, 'eventos/actualizarEvent.html', {'form': form})

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

def menuConsultas(request):
    return render (request, 'consultasAvanzadas/menu.html')

def consultaUsuarios(request):
    evento_id = request.GET.get('evento_id') 
    if evento_id:
        usuarios_registrados = RegistroEvento.objects.filter(evento_id=evento_id).count()
    else:
        usuarios_registrados = None

    eventos = Evento.objects.all()
    return render(request, 'consultasAvanzadas/usuarios.html', {
        'usuarios_registrados': usuarios_registrados,
        'eventos': eventos
    })


def consultaOrganizacion(request):
    usuario_id = request.GET.get('usuario_id')
    eventos_organizados = 0
    if usuario_id:
        eventos_organizados = Evento.objects.filter(organizador_id=usuario_id).count()

    usuarios = Usuario.objects.all()
    return render(request, 'consultasAvanzadas/organizacion.html', {
        'eventos_organizados': eventos_organizados,
        'usuarios': usuarios
    })


def consultaEventos(request):
    ahora = timezone.now()
    mes_actual = ahora.month
    anio_actual = ahora.year
    
    eventos_mes = Evento.objects.filter(fecha__month=mes_actual, fecha__year=anio_actual).count()
    
    return render(request, 'consultasAvanzadas/eventos.html', {
        'eventos_mes': eventos_mes
    })
