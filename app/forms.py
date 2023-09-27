from django import forms
from django.forms import ModelForm
from .models import *

class PictureForm(forms.ModelForm):
    
    class Meta:
        model = Picture
        fields = ('name', 'production_year', 'price', 'image')

class ArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = ('name', 'surname', 'pictures')