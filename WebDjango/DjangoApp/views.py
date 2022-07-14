from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from DjangoApp.models import *
from .forms import *




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

def base(request):     
    return render(request, 'DjangoApp/base.html')


def index(request):
    return render(request, 'DjangoApp/index.html')

def contacto(request):
    return render(request, 'DjangoApp/contacto.html')

def portfolio(request):
    return render(request, 'DjangoApp/portfolio.html')

def blog(request):
    post = Post.objects.all()
    ctx = {"post": post}
    return render(request, 'DjangoApp/blog.html', ctx)

def blogSingle(request, post_id):
    post = Post.objects.get(id=post_id)
    ctx = {"post": post}
    return render(request, 'DjangoApp/blogSingle.html', ctx)

def acerca(request):
    return render(request, 'DjangoApp/acerca.html')

def servicios(request):
    servicios = Servicios.objects.all()
        
    ctx = {"servicios": servicios} 
    return render(request, 'DjangoApp/servicios.html', ctx)

# -----Vistas Auxiliares-----------

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


  
def crearPost(request):   
    
    if request.method == "POST":
        form = CrearPost(request.POST)
        if form.is_valid():
            form.save()
    
            ctx = {"form": form,}
            return redirect('blog')       
           
        
    else:
        form = CrearPost()    
    
          
    
    ctx = {"form": form,}  
    return render(request, 'DjangoApp/crearPost.html' ,ctx)
    
    
def eliminarPost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog')

def editarPost(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = crearPost(request.POST)
        if form.is_valid():            
            post_info = form.cleaned_data.get
            post.titulo = post_info['titulo']
            post.imagen = post_info['imagen']
            post.post = post_info['post']
            post.autor = post_info['autor']
            post.fecha = post_info['fecha']
            post.save()
            return redirect('blogSingle')
        
                
        else:
            return render(request, 'DjangoApp/editarPost.html', {'form': form, 'post':post})      
        
        
    formEditar = crearPost(initial={'titulo': post.titulo, 'imagen': post.imagen, 'post': post.post, 'autor': post.autor, 'fecha': post.fecha})
        
              
    
    return render(request, 'DjangoApp/editarPost.html', {'form': formEditar, 'post':post}) 