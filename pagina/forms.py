from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
            model = Productos
            fields = ('idconcepto','observacion','entrada','salida',)