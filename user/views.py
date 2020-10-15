from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
	username=''
	password=''
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user != None:
			login(request, user)
			return HttpResponseRedirect(reverse('library:index'))
		else:
			messages.warning(request, 'Invalid username/password')
	return render(request, 'user/login.html',{'usn':username, 'pwd':password})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('library:index'))

def profile(request):
	return render(request, 'user/profile.html')

def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		repeated_password = request.POST['repeated_password']
		if repeated_password == password:
			try:
				user=User.objects.create_user(username, '', password)
				login(request,user)
				return HttpResponseRedirect(reverse('library:index'))
			except:
				messages.warning(request, 'Username already exists!')
		else:
			messages.warning(request, 'Passwords do not match!')
	return render(request, 'user/register.html')