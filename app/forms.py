from django import forms
from .models import Task
from datetime import date

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateInput(format=('%Y-%m-%d'), 
            attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date', 'style': 'width:150px;', 'min': date.today()}),
        }
