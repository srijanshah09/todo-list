from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'todo/home.html')

def register(request):
	return render(request, 'todo/register.html')

def index(request):
	return render(request, 'todo/index.html')		