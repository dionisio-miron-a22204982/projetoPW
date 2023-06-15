from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo...'}),
            'conteudo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o conteúdo...'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome...'}),
            'datacriacao': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome...'}),
        }

        # o dicionário labels especifica o texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }
        