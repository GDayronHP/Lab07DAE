# forms.py
from django import forms
from .models import Usuario, Evento, RegistroEvento

class LoginForm(forms.Form):
    nombres = forms.CharField(max_length=100)
    contraseña = forms.CharField(widget=forms.PasswordInput)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'sexo', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'organizador', 'capacidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'organizador': forms.Select(attrs={'class': 'form-select'}),  # Cambia 'Select' por 'MultipleChoiceField' si es necesario
        }

class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = ['evento', 'usuario']

class UpdateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'sexo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class UpdateEventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'capacidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
