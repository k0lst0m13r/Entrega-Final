from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from DjangoApp.models import *
from .forms import *
from datetime import date
from datetime import datetime




######  REGISTRO - LOGIN - LOGOUT  #######

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    form =  AuthenticationForm()
    ctx = {"form": form}
    return render(request, 'DjangoApp/login.html',ctx)

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')

            return redirect('index')

        return render(request, 'DjangoApp/registro.html', {"form": form})


    else:
        form = UserRegisterForm()
    return render(request, 'DjangoApp/registro.html', {"form": form})


def log_out(request):
    logout(request)
    return redirect('index')




############## VISTAS PRINCIPALES ################


def base(request):
    return render(request, 'DjangoApp/base.html')


def index(request):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "DjangoApp/media/avatar/user_default.png"
        return render(request, 'DjangoApp/index.html', {'url': url})

    return render(request, 'DjangoApp/index.html')


def portfolio(request):
    return render(request, 'DjangoApp/portfolio.html')


def acerca(request):
    return render(request, 'DjangoApp/acerca.html')


def servicios(request):
    servicios = Servicios.objects.all()

    ctx = {"servicios": servicios}
    return render(request, 'DjangoApp/servicios.html', ctx)

################## PERFIL ##################

@login_required
def perfil(request):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "DjangoApp/media/avatar/user_default.png"
        return render(request, 'DjangoApp/perfil.html', {'url': url})

    return render(request, 'DjangoApp/perfil.html',)

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            usuario.username = info['username']
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']

            usuario.save()

            return redirect('perfil')
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email':usuario.email, 'first_name':usuario.first_name, 'last_name': usuario.last_name,})

    ctx = {'form': form,}
    return render(request, 'DjangoApp/editarPerfil.html', ctx)


def avatar(request):
    if request.method == "POST":
        form = EditarAvatar(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(imagen=form.cleaned_data['imagen'])
            avatar.save()
            return redirect('perfil')

    else:
        form = EditarAvatar()

    ctx = {"form": form}
    return render(request, 'DjangoApp/avatar.html' ,ctx)





#----------- sección blog -------------#

def blog(request):
    post = Post.objects.all()
    ctx = {"post": post}
    return render(request, 'DjangoApp/blog.html', ctx)

def blogSingle(request, post_id):
    post = Post.objects.get(id=post_id)
    comentarios = Comentarios.objects.all()
    ctx = {"post": post, "comentarios": comentarios}


    return render(request, 'DjangoApp/blogSingle.html', ctx)



############## VISTAS AUXILIARES ##########

def comentarios(request):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')

    else:
        form = CommentForm()

    ctx = {"form": form}
    return render(request, 'DjangoApp/comentarios.html' ,ctx)


@staff_member_required
def agregarServicio(request):

    if request.method == "POST":
        form = ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicios')

    else:
        form = ServiciosForm()

    ctx = {"form": form}
    return render(request, 'DjangoApp/agregarServicio.html' ,ctx)


#------------- sección post --------------#

@staff_member_required
def crearPost(request):

    if request.method == "POST":
        form = CrearPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            ctx = {"form": form,}
            return redirect('blog')
    else:
        form = CrearPost()

    ctx = {"form": form,}
    return render(request, 'DjangoApp/crearPost.html' ,ctx)

@staff_member_required
def eliminarPost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog')


@staff_member_required
def editarPost(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CrearPost(request.POST, request.FILES)
    if request.method == 'POST':
        form = CrearPost(request.POST, request.FILES)
        if form.is_valid():
            post_info = form.cleaned_data.get
            post.titulo = post_info('titulo')
            post.imagen = post_info('imagen')
            post.post = post_info('post')
            post.autor = post_info('autor')
            post.fecha = datetime.now()
            post.save()
            return redirect('blog')

        else:
            return render(request, 'DjangoApp/editarPost.html', {'form': form, 'post':post})

    form = CrearPost(initial={'titulo': post.titulo, 'imagen': post.imagen, 'post': post.post, 'autor': post.autor, 'fecha': post.fecha})

    return render(request, 'DjangoApp/editarPost.html', {'form': form, 'post':post})
