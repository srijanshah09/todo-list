from django.urls import path

from .import views


urlpatterns = [
	path('', views.home, name='home'),
	path('home/', views.home, name='home'),
	path('register/', views.register, name='register'),
	path('account/', views.index, name='index'),
	path('addTask/',views.addTask, name='addTask'),
	path('deleteCompleted/',views.deleteCompleted, name='deleteCompleted'),
	path('deleteAll/',views.deleteAll, name='deleteAll'),
	path('updateStatus/<int:id>/',views.updateStatus,name='updateStatus'),	
]