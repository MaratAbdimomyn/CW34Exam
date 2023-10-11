from distutils.command.clean import clean
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *
from django import forms

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
        if x > 2023:
            message = "Картина должна быть не позднее 2023 года"
            raise forms.ValidationError(message)
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