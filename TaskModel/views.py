from django.shortcuts import render,redirect
from . import forms
from . import models

# from ..TaskCategory import forms 
# Create your views here.

def add_task(request):
    
    task_form=forms.TaskForm()
    if request.method=='POST':
        task_form=forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return  redirect('home')
    return render(request, 'TaskModel/add_task.html',{'form':task_form})



def edit_task(request,id):

    task_id=models.Task.objects.get(pk=id)
    task_instance=forms.TaskForm(instance=task_id)

    if request.method=='POST':
        task_instance=forms.TaskForm(request.POST,instance=task_id)

        if task_instance.is_valid():
            task_instance.save()
            return redirect('home')
    return render(request, 'TaskModel/add_task.html',{'form':task_instance})


def delete_task(request,id):

    task_id=models.Task.objects.get(pk=id)
    task_id.delete()
    return redirect('home')


