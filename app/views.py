from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.filter(task_owner=request.user).order_by('deadline')

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(False)
            new_task.task_owner = request.user
            new_task.save()
            messages.success(request, "Task added successfully")
            return redirect('/')
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
     }   
    return render(request, 'app/home.html', context)

def edit(request, task_id):
    return render(request, 'app/edit.html')

def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully")
        return redirect('/')
        
    return render(request, 'app/delete.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'app/login.html')

def signup(request):
    return render(request, 'app/signup.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out!")
    return redirect('login')