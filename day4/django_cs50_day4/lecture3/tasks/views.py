from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#lecture 3 is done
# tasks = ['foo','bar','baz']
# tasks = [] #this is global variable, it shows all tasks to everyone, 
# we need to create variable in sessions in order to show specific tasks to each user in index 

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    # priority = forms.IntegerField(label = "Priority", min_value=1,max_value=3)
    # so in the client side max min value will be checked and will require 2 values to be inserted - it ll not happen with db, on client side it ll be solved
    #server side validation will be in the add function

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = [] #we are taking tasks from session of each client


    return render(request, 'tasks/index.html',{
        "tasks" : request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # tasks.append(task) - it s used for global variable of tasks

            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form" : form
            })

    return render(request, "tasks/add.html", 
                  {"form" : NewTaskForm()})