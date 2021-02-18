# from django import forms
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse

# # tasks = [] #stored all tasks in a global variable 

# class NewTaskForm(forms.Form):
#     task = forms.CharField(label="New Task")
#     # priority = forms.IntegerField(label="Priority", min_value=1, max_value=4)

# # Create your views here.

# def index(request):
#     if "tasks" not in request.session: #if no list of tasks in session, create empty list of tasks.
#         request.session["tasks"] = []

#     return render(request, "todo/index.html", {
#         "tasks": request.session["tasks"] #render session to pass in list of tasks to template
#     })

# def add(request):
#     if request.method == "POST": #if the form is valid...
#         form = NewTaskForm(request.POST) #creates a blank form when parenthesis are empty. request.POST contains all the data the user submits when they submit the form.
#         if form.is_valid():
#             task = form.cleaned_data["task"] #access to all data user has submited
#             # tasks.append(task) #add this task to list of tasks 
#             request.session["tasks"] += [task]
#             return HttpResponseRedirect(reverse("tasks:index"))

#         else:
#             return render(request, "todo/add.html", {
#                 "form": form #send back existing form data
#             })

#     return render(request, "todo/add.html", {
#         "form": NewTaskForm()
#     })