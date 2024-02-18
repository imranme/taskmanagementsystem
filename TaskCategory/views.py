from django.shortcuts import render,redirect
from . import forms 


def add_category(request):

    category_form=forms.CategoryForm()
    
    if request.method == 'POST':
        category_form=forms.CategoryForm(request.POST)

        if category_form.is_valid():
            category_form.save()
            return redirect('home')
        
    return render(request,'TaskCategory/add_category.html',{'form':category_form})


