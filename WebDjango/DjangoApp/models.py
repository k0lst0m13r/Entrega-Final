from django.db import models
from django.contrib.auth.models import User



class Comentarios(models.Model):
    nombre = models.CharField(max_length=40)
    comentario = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Servicios(models.Model):
    servicio = models.CharField(max_length=30)
    def __str__(self):
        return self.servicio


class Post(models.Model):
    titulo = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="blog/", null=True)
    post = models.TextField()
    autor = models.CharField(max_length=40)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Autor: {self.autor} - Titulo: {self.titulo}"


class Avatar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar/', null=True, blank=True)
    def __str__(self):
        return f"Usuario: {self.usuario}"
