from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

import json

from .models import Item, hasCategory, Wardrobe

from .forms import LoginForm, RegForm

# Create your views here.

"""def index(request):
	users = User.objects.get(username="admin")
	return render(request, 'modifit/index.html', { 'users' : users })"""

"""from django.contrib.auth.decorators import login_required
@login_required(login_url='/') #if not logged in redirect to /
def catalogue(request):		
	return render(request, 'modifit/catalogue.html')"""

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
	if request.user.is_authenticated():
		return HttpResponseRedirect('/wardrobe/')
	else:
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
						return HttpResponseRedirect('/wardrobe/')
					else:
						error_message = "Your account is inactive."
				else:
					error_message = "Username or password incorrect."
		else:
			form = LoginForm()

		return render_to_response( 'modifit/index.html', { 'form': form, 'error_message': error_message }, context_instance=RequestContext(request) )

@login_required(login_url='/') #if not logged in redirect to /
def logging_out(request):
	logout(request)
	return render( request, 'modifit/logout.html' )

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/wardrobe/')
	else:
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
	if request.user.is_authenticated():
		return HttpResponseRedirect('/wardrobe/')
	else:
		return render(request, 'modifit/reg_success.html')


@login_required(login_url='/')
def catalogue(request, category_name=None):
	current_user = request.user
	if current_user.first_name != '':
		name = current_user.first_name
	else:
		name = current_user.username

	categorized = hasCategory.objects.all()
	"""categorizedItems = []
	for i in categorized:
		categorizedItems.append(i.item)"""

	wardrobe = Wardrobe.objects.filter(user_id=request.user.id)
	wardrobeItems = []
	for i in wardrobe:
		wardrobeItems.append(i.item)

	allFilteredCategorizedItems = [i for i in categorized if i.item not in wardrobeItems]

	#items = [i for i in categorizedItems if i not in wardrobeItems]
	#print "Category name: " + str(category_name)
	if category_name is not None:
		filteredCategorizedItems = [i for i in allFilteredCategorizedItems if i.category.name == category_name]
	else:
		filteredCategorizedItems = allFilteredCategorizedItems

	categories = list(set([i.category for i in allFilteredCategorizedItems]))

	return render( request, 'modifit/catalogue.html', { 'name': name, 'items': filteredCategorizedItems, 'categories' : categories } )


@login_required(login_url='/')
def rate(request):
	if request.POST:
		item = request.POST.get('itemToRate')
		rate = request.POST.get('rating')
		response_data = {}

		wardrobe = Wardrobe.objects.get( user_id=request.user.id, item_id=item )
		wardrobe.rating = rate
		wardrobe.save()

		response_data['result'] = 'Rate item successful!'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

		"""for i in Item.objects.all():

			rate = request.POST.get('rate' + str(i.id))
			if rate is None:
				continue

			item_id = request.POST.get('item_id_' + str(i.id))
			if item_id is not None:
				try:
					wardrobe = Wardrobe.objects.get(user_id=request.user.id, item_id=item_id)
					wardrobe.rating = rate
					wardrobe.save()
				except Wardrobe.DoesNotExist:
					wardrobe = Wardrobe( user_id=request.user.id, item_id=i.id, rating=int(rate) )
					wardrobe.save()"""
					
		"""
		rate = request.POST.get('rate'+str(1))
		item_id = request.POST.get('item_id_' + str(1))
		item_id = Wardrobe.objects.get(item_id=int(item_id)).exists()
		name = request.user.username
		user_id = request.user.id
		#item = Item.objects.get(pk=1)
		#item_id = item.id
		return render(request, 'modifit/test.html', { 'name' : name, 'user_id' : user_id, 'item_id' : item_id, 'rate' : rate })
		"""
		#return HttpResponseRedirect('/wardrobe/')

@login_required(login_url='/')
def remove_from_wardrobe(request):
	if request.POST:
		item = request.POST.get('itemToRemove')
		response_data = {}

		wardrobe = Wardrobe.objects.get( user_id=request.user.id, item_id=item ).delete()

		response_data['result'] = 'Delete item successful!'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

@login_required(login_url='/')
def add_to_wardrobe(request):
	if request.POST:
		item = request.POST.get('itemToAdd')
		response_data = {}

		wardrobe = Wardrobe( user_id=request.user.id, item_id=item )
		wardrobe.save()

		response_data['result'] = 'Add item successful!'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)

@login_required(login_url='/')
def wardrobe(request):
	current_user = request.user
	if current_user.first_name != '':
		name = current_user.first_name
	else:
		name = current_user.username
	wardrobe = Wardrobe.objects.filter(user_id=request.user.id)
	return render(request, 'modifit/wardrobe.html', { 'name' : name, 'wardrobe' : wardrobe })