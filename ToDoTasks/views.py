from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm

from django.contrib import messages

def returnHomePage(request):
    # rendering data => query them then show them in html tag
    all_tasks = Tasks.objects.all()

    task_form = TaskForm()

    # which is always True cuz request == POST means we will write in the model !
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, 'has been added successfully to DB')

            return redirect('task')
    context = {
        'tasks': all_tasks,
        'task_from': task_form
    }
    return render(request, 'TASKS/create_task.html', context)

# a view == think of a new url, no matter what will be returned
def deleteTask(request, pk_):

    a_specific_task_chosen = Tasks.objects.get(id=pk_)

    if request.method == "POST":
        a_specific_task_chosen.delete()
        return redirect('task')
    context = {
        'the_delete_one': a_specific_task_chosen
    }
    return render(request, 'TASKS/delete_task.html', context)

def updateTask(request, pk_):
    a_specific_task_chosen = Tasks.objects.get(id=pk_)
    task_form = TaskForm(instance=a_specific_task_chosen)

    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=a_specific_task_chosen)
        if task_form.is_valid():
            task_form.save()
            return redirect('task')

    context = {
        'task_form': task_form
    }

    return  render(request, 'TASKS/update_task.html', context)