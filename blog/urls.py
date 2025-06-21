from django.urls import path
from .import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('about/' , views.about , name='about'),
    path('login/' , views.login_page , name='login'),
    path('add_post/' , views.add_post , name='add_post'),
    path('register/' , views.register , name='register'),
]