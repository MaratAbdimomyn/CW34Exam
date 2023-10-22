from distutils.command.clean import clean
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView

class SignUp(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Учетная запись создана'

    """def post(self, request, *args, **kwargs):
        q = UserCreationForm(request.POST)
        w = request.POST['password1']
        e = request.POST['password2']
        if w != e:
            message = "Пароли должны быть одинаковые"
            raise forms.ValidationError(message)
        if q.is_valid():
            q.save()"""

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('home')

class PictureView(ListView):
    model = Picture
    template_name = 'home.html'
    context_object_name = 'one1'

class AboutPicture(DetailView):
    model = Picture
    template_name = 'about.html'
    context_object_name = 'one2'

class CreatePicture(CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        data = PictureForm(request.POST)
        x = int(request.POST['production_year'])
        z = int(request.POST['price'])
        if x > 2023:
            message = "Картина должна быть не позднее 2023 года"
            raise forms.ValidationError(message)
        if z <= 0:
            message2 = "Цена картины не может быть отрицательной"
            raise forms.ValidationError(message2)
        if data.is_valid():
            data.save()
        else:
            return HTTPResponse('asdasdasdas')
        return redirect('home')

class DeletePicture(DeleteView):    
    model = Picture
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
    


class ArtistView(ListView):
    model = Artist
    template_name = 'artist.html'
    context_object_name = 'one3'

class CreateArtist(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'create_artist.html'
    success_url = reverse_lazy('artist')