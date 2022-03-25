from django import forms
from .models import Noticia

class forms_noticias(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'categoria', 'contenido', 'imagen_referencial']