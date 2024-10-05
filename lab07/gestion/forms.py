# forms.py
from django import forms
from .models import Usuario, Evento, RegistroEvento

class LoginForm(forms.Form):
    nombres = forms.CharField(max_length=100)
    contraseña = forms.CharField(widget=forms.PasswordInput)

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'capacidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
        
class UpdateEventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'capacidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
        
class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = ['evento', 'usuario']



    
