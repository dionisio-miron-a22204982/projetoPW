from django.db import models



# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    conteudo = models.CharField(max_length=500)
    datacriacao = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.titulo[:30]

