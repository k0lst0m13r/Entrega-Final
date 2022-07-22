from django.test import TestCase
from .models import *

class ComentariosTest(TestCase):
    def setup(self):
        Comentarios.objects.create(nombre="Tete", comentario="Comentario de testeo" )

    def comentario_nombre(self):
        comentario = Comentarios.objects.get(comentario)
        self.assertEqual(comentario.nombre, "Tete")

    def comentario_nombre(self):
        comentario = Comentarios.objects.get(nombre)
        self.assertEqual(comentario.nombre, "admin")

class ServiciosTest(TestCase):
    def setup(self):
        Servicios.objects.create("Back end")


    def test_servicio(self):
        serv = Servicios.objects.get(servicio)
        self.assertEqual(serv.servicio)

    def test_servicio(self):
        serv = Servicios.objects.get(servicio)
        self.assertNotEqual(serv.servicio)

# Create your tests here.
