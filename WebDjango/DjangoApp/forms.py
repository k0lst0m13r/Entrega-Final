from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CommentForm(ModelForm):

    class Meta:
        model = Comentarios
        fields = ('nombre', 'comentario',)


class ServiciosForm(ModelForm):

    class Meta:
        model = Servicios
        fields = ('servicio',)


class CrearPost(ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'imagen', 'post', 'autor',)



class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
