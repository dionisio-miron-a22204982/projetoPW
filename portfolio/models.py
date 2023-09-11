from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    conteudo = models.CharField(max_length=500)
    datacriacao = models.DateTimeField(auto_now_add=True)

    

# Create your models here.
