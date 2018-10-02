from django import forms

from django.contrib.auth.models import User
from .models import Task

class LoginForm(forms.ModelForm):
	class  Meta:
		model = User
		fields = ['username','password']
		widgets = {
			'username': forms.TextInput(
				attrs={'class':'form-control', id:'username', 'aria-describedby':'emailHelp', 'placeholder':'Username'}
				),
			'password': forms.PasswordInput(
				attrs={'class':'form-control', id:'password', 'aria-describedby':'emailHelp', 'placeholder':'Password'}
				)

		}

class RegistrationForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput(
				attrs={
				'class':'form-control', 
				id:'password1', 
				'aria-describedby':'emailHelp', 
				'placeholder':'Re-enter Password'}
				), required=True, max_length=128)

	class Meta():
		model = User
		fields = ['username','password','password1']
		widgets = {
			'username': forms.TextInput(
				attrs={'class':'form-control', id:'username', 'aria-describedby':'emailHelp', 'placeholder':'Enter Username'}
				),
			'password': forms.PasswordInput(
				attrs={'class':'form-control', id:'password', 'aria-describedby':'emailHelp', 'placeholder':'Enter Password'}
				),
			}

