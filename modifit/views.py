from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	users = User.objects.get(username="admin")
	return render(request, 'modifit/index.html', { 'users' : users })

def wardrobe(request, wardrobe_id):
	response = "Wardrobe ID: " + str(wardrobe_id)
	user = 1;
	return render(request, 'modifit/wardrobe.html', { 'response' : response, 'user' : user })