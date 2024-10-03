# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario  # Asegúrate de importar tu modelo Usuario
from .forms import LoginForm  # Importa tu formulario de login

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            contraseña = form.cleaned_data['contraseña']
            
            try:
                usuario = Usuario.objects.get(nombres=nombres)  # Busca el usuario por nombre
                if usuario.check_password(contraseña):  # Verifica la contraseña
                    # Aquí puedes establecer la sesión o hacer otra lógica
                    messages.success(request, "Inicio de sesión exitoso.")
                    return redirect('menu.html')
                else:
                    messages.error(request, "Contraseña incorrecta.")
            except Usuario.DoesNotExist:
                messages.error(request, "El usuario no existe.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})  # Renderiza tu template

def menu(request):
    return render(request, 'menu.html')