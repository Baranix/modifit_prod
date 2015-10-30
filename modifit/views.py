from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import LoginForm, RegForm

# Create your views here.

"""def index(request):
	users = User.objects.get(username="admin")
	return render(request, 'modifit/index.html', { 'users' : users })"""

"""from django.contrib.auth.decorators import login_required
@login_required(login_url='/') #if not logged in redirect to /
def home(request):		
	return render(request, 'modifit/home.html')"""

"""def index(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're successfully logged in!"
			else:
				state = "Your account is not active, please contact the site admin."
		else:
			state = "Your username and/or password were incorrect."

	return render_to_response('modifit/index.html', {'state':state, 'username': username}, context_instance=RequestContext(request))"""

def index(request):
	error_message = ''
	username = password = ''
	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/home/')
				else:
					error_message = "Your account is inactive."
			else:
				error_message = "Username or password incorrect."
	else:
		form = LoginForm()

	return render_to_response( 'modifit/index.html', { 'form': form, 'error_message': error_message }, context_instance=RequestContext(request) )


@login_required(login_url='/') #if not logged in redirect to /
def home(request):
	current_user = request.user
	if current_user.first_name != '':
		name = current_user.first_name
	else:
		name = current_user.username
	return render( request, 'modifit/home.html', { 'name': name } )

@login_required(login_url='/')
def logging_out(request):
	logout(request)
	return render( request, 'modifit/logout.html' )

def register(request):
	error_message = ''
	if request.POST:
		form = RegForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			email = request.POST.get('email')
			password = request.POST.get('password')
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')

			if username and email and password:
				newUser = True
				if User.objects.filter(username=username).exists():
					error_message = error_message + "Username already exists. "
					newUser = False
				if User.objects.filter(email=email).exists():
					error_message = error_message + "Email already in use. "
					newUser = False
				if( newUser ):
					user = User.objects.create_user(
							username=username,
							email=email,
							password=password,
							first_name=first_name,
							last_name=last_name
						)
					return HttpResponseRedirect('/reg_success/')

			elif username is None:
				error_message = error_message + "Username is missing! "
			elif password is None:
				error_message = error_message + "Password is missing! "
			elif email is None:
				error_message = error_message + "Email address is missing! "
			else:
				error_message = error_message + "An unknown error has occurred! Please email me immediately at nikki.ebora@gmail.com "
	else:
		form = RegForm()

	return render_to_response( 'modifit/register.html', { 'form': form, 'error_message': error_message }, context_instance=RequestContext(request) )

def reg_success(request):
	return render(request, 'modifit/reg_success.html')


def wardrobe(request, wardrobe_id):
	response = "Wardrobe ID: " + str(wardrobe_id)
	user = 1;
	return render(request, 'modifit/wardrobe.html', { 'response' : response, 'user' : user })