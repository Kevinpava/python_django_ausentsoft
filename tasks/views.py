from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': CustomUserCreationForm(),
                    "error": 'este usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm(),
            "error": 'contraseña no coincide'
        })
   

def tasks(request):
    tasks = Task.objects.filter(user=request.user, completed_at__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks})

def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user,completed_at__isnull=False )
    return render(request, 'completed_tasks.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed_at = timezone.now()
    task.save()
    return redirect('completed_tasks')

def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html',{
        'form': TaskForm
        
    })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
             return render(request,'create_task.html',{
            'form': TaskForm,
            'error': 'porfavor pruebe con valor valido'
         })
 
def signout(request):
    logout(request)
    return redirect('home')
   
def signin(request):
  if request.method == 'GET': 
        return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
  else:
      user = authenticate(request,username =request.POST['username'], password=request.POST['password'])
      if user is None:
            return render(request, 'signin.html', {
          'form': AuthenticationForm,
          'error': 'Username or password is incorrect'
      })

      else:
          login(request,user)
          return redirect('tasks')
          
def task_detail(request,task_id):
    if request.method == 'GET':
        task =  get_object_or_404(Task,pk=task_id,user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form} )
    else:
        try:
            task = get_object_or_404(Task,pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'Error': 'Error Actualizando'} )



def delete_task(request, task_id):
   task =  get_object_or_404(Task,pk=task_id,user=request.user)
   if request.method == 'POST':
       task.delete()
       return redirect('tasks')

    

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')





