from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *
from django.shortcuts import get_object_or_404

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

class DeletePicture(DeleteView):    
    model = Picture
    template_name = 'delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
    