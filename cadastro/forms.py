
from django import forms

from .models import Usuarios

class UserForm(forms.ModelForm):

    class Meta:
        model = Usuarios

        fields = ('nome', 'telefone', 'email', 'cep', 'cidade', 'iptu')
        widgets = {'nome': forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'placeholder': 'Nome Completo'}),
                   'telefone': forms.TextInput(attrs={'id': 'telefone', 'class': 'form-control', 'placeholder': 'Telefone'}),
                   'email': forms.TextInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
                   'cep': forms.TextInput(attrs={'id': 'cep', 'class': 'form-control', 'placeholder': 'CEP'}),
                   'cidade': forms.TextInput(attrs={'id': 'cidade', 'class': 'form-control', 'placeholder': 'Cidade'}),
                   'iptu': forms.TextInput(attrs={'id': 'iptu', 'class': 'form-control', 'placeholder': 'Cadastro de propriedade rural (IPTU)'})
                   }
        required = True