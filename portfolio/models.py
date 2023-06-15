from django.db import models

from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    conteudo = models.CharField(max_length=500)
    datacriacao = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.titulo
    

# Create your models here.
