from django import forms 
from .models import ToDo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']
        
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["title","completed"]        