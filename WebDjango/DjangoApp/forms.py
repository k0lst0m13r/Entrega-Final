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

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    #images = forms.ImageField(upload_to="perfil/", null=True)
    first_name = models.CharField()
    last_name = models.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)

class UserEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2', 'first_name', 'last_name',]
