from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms  import *
from .models import Task

import datetime

# Create your views here.
def home(request):
	if request.POST:
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			username_auth = User.objects.filter(username__exact=username)
			if not username_auth:
				error = 'Invalid Username'	
			else:
				error = 'Incorrect Password'	
			form = LoginForm()
			context = {'form' : form, 'error': error}
			return render(request, 'todo/home.html', context)
		

	else:		
		form = LoginForm()
		context = {'form' : form}
		return render(request, 'todo/home.html', context)


def register(request):
	if request.POST:
		form = RegistrationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		password1 = request.POST['password1']
		if User.objects.filter(username__exact=username):
			error = 'Username unavailable. Please try another.'
		elif password != password1:
			error = 'Passwords do not match. Please try again'
		else:
			User.objects.create_user(username=username,password=password)
			return redirect('home')	
		
		form = RegistrationForm()
		context = {'form':form, 'error':error}
		return render(request, 'todo/register.html', context)
	
	else:
		form = RegistrationForm()
		context = {'form' : form }
		return render(request, 'todo/register.html', context)
		

@login_required(login_url="/")
def index(request):
	user = request.user
	if request.POST.get('search_date') is None or request.POST.get('search_date') == '':
		date = datetime.datetime.now().date()
	else:
		date = request.POST.get('search_date')
		date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

	tasks= Task.objects.filter(user_id__exact=user,task_date__exact=date)
	context = {'tasks':tasks, 'date':date}
	return render(request, 'todo/index.html',context)


@login_required(login_url='/')
def addTask(request):
	user = request.user
	task_type = request.POST.get('task_type')
	task_date = request.POST.get('task_date')
	task_text = request.POST.get('task_text')
	task_priority = request.POST.get('task_priority')
	task = Task(user_id=user.id,task_type=task_type,task_date=task_date,task_text=task_text,task_priority=task_priority)
	task.save()	
	return redirect('index')


@login_required(login_url='/')
def deleteCompleted(request):
	selected_date = request.POST.get('selected_date')
	task_type = request.POST.get('task_type')
	print(selected_date)
	#tasks = Task.objects.filter(user_id=request.user.id).filter(task_date__exact=selected_date).filter(task_type__exact=task_type).filter(task_status=True)
	#tasks.delete()
	return redirect('index')


@login_required(login_url='/')
def deleteAll(request):
	selected_date = request.POST.get('selected_date')
	task_type = request.POST.get('task_type')
	tasks = Task.objects.filter(user_id=request.user.id).filter(task_date__exact=selected_date).filter(task_type__exact=task_type)	
	tasks.delete()
	return redirect('index')	


@login_required(login_url='/')
def updateStatus(request,id):
	task= Task.objects.get(id=id)
	if task.task_status == True:
		task.task_status = False
	else:
		task.task_status = True
	task.save()	
	return redirect('index')