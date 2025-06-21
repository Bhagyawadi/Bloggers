from django.shortcuts import render , redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth import aauthenticate , login
from django.contrib.auth.models import User

# Create your views here.


def home(request) :  
     
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }    
    return render(request , 'blog/home.html' , context)


def about(request) :
    return render(request , 'blog/about.html')


def login_page(request) :
    
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists() :
            messages.info( request , 'Invalid Username')
            return redirect('/login/')
        
        user = aauthenticate(username = username , password = password)
        
        if user is None :
            messages.info( request , 'Invalid Password')
            return redirect('/login/')
        
        else :
            login(request , user)
            return redirect('/')
                 
    return render(request , 'blog/login.html')


def add_post(request) :
    if request.method == 'POST' :
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        posts = Post(title = title , content = content)
        posts.save()
        return redirect('/')
    return render(request , 'blog/add_post.html')


def register(request) :
    if  request.method == 'POST' :
        first_name =  request.POST.get('first_name')
        last_name =  request.POST.get('last_name')
        username =  request.POST.get('username')
        password =  request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists() :
            messages.info( request , 'Username already taken')
            return redirect('/register/')
    
        user = User.objects.create(
            first_name = first_name , 
            last_name = last_name , 
            username = username , 
        )
        
        user.set_password(password)
        user.save()
        
        messages.info( request , 'Account Created Successfully')
        return redirect('/register/')
    
    return render( request , 'blog/register.html')  