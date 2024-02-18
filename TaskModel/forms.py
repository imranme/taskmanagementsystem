from .models import Task 
from django import forms 

class TaskForm(forms.ModelForm):
    
    class Meta:

        model=Task
        fields='__all__'

        labels={
            'Title':'Enter Task Title',
            'Description':'Enter Task Description',
            'IsCompleted':'is task completed or not ?',
            'AssignDate':'Enter Assigned Date',
        }
        widgets = {
                'AssignDate': forms.DateInput(attrs={'type': 'date'}),
            }
