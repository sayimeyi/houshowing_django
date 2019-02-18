from django.urls import path

from . import views

app_name = 'houshowing'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('home', views.home, name='home'),

]