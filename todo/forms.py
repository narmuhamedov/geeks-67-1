from django import forms
from . import models

class TodoForm(forms.ModelForm):
    class Meta:
        model = models.TodoModel
        #2 слеша
        fields = '__all__'