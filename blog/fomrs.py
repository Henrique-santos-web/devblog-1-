from django import forms
from .models import MensagemContato

class Contatoform(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'mensagem']