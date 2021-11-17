from django import forms
from testapp.models import Movies
class AddMovies(forms.ModelForm):
    class Meta:
        model=Movies
        fields ='__all__'
