from django.forms import ValidationError, ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('name', 'production_year', 'price', 'image')

    """def clean_production_year(self):
        year = self.cleaned_data['production_year']
        if year < 1900:
            msg = "Модель должна быть старше 1900 года"
            raise forms.ValidationError(msg)
        return year"""


class ArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = ('name', 'surname', 'pictures')