from django import forms 
from .models import ToDo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = ToDo
        field = ['title']