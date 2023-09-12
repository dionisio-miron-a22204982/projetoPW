from django.urls import reverse
from django.db import models


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    conteudo = models.CharField(max_length=500)
    datacriacao = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.titulo[:30]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    

class Project(models.Model):
    titulo = models.CharField(max_length=30)
    authores = models.CharField(max_length=40)
    conteudo = models.CharField(max_length=500)
    datacriacao = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200)

    
    def __str__(self):
        return self.titulo[:30]
    
class Course(models.Model):
    titulo = models.CharField(max_length=40)
    ano = models.CharField(max_length=1)
    semester = models.CharField(max_length=10)
    etc = models.CharField(max_length=2)

    
    def __str__(self):
        return self.titulo[:30]