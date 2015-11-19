from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

import json

from .models import Item, hasCategory, Wardrobe, hasAttribute
from .models import Sweater_Type, Jacket_Type, Blazer_Type, Sweatshirt_Type, Jumpsuit_Type, Style, Color, Pattern, Material, Silhouette, Outerwear_Structure, Pants_Structure, Decoration, Neckline, Sleeve_Length, Sleeve_Style, Top_Length, Pants_Length, Shorts_Length, Skirt_Length, Fit_Type, Waist_Type, Top_Closure_Type, Outerwear_Closure_Type, Bottom_Closure_Type, Front_Style

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

	return render( request, 'modifit/catalogue.html', { 'name': name, 'items': filteredCategorizedItems, 'categories' : categories, 'current_category' : category_name } )


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

		try:
			wardrobe = Wardrobe.objects.get(user_id=request.user.id, item_id=item)
			response_data['result'] = 'Item is already in the Wardrobe!'
		except Wardrobe.DoesNotExist:
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

	#categorized = hasCategory.objects.all()

	#items = [i for i in categorizedItems if i not in wardrobeItems]
	#print "Category name: " + str(category_name)
	"""if category_name is not None:
		filteredCategorizedItems = [i for i in wardrobe_items if i.category.name == category_name]
	else:
		filteredCategorizedItems = wardrobe_items

	categories = list(set([i.category for i in allFilteredCategorizedItems]))"""

	return render(request, 'modifit/wardrobe.html', { 'name' : name, 'wardrobe' : wardrobe })

def item(request, item_id=None):
	if item_id is not None:
		item = Item.objects.get(pk=item_id)
		category = hasCategory.objects.get(item_id=item_id).category
		attributes = hasAttribute.objects.filter(item_id=item_id)

		attribute_set = []
		attribute_tables = [Sweater_Type, Jacket_Type, Blazer_Type, Sweatshirt_Type, Jumpsuit_Type, Style, Color, Pattern, Material, Silhouette, Outerwear_Structure, Pants_Structure, Decoration, Neckline, Sleeve_Length, Sleeve_Style, Top_Length, Pants_Length, Shorts_Length, Skirt_Length, Fit_Type, Waist_Type, Top_Closure_Type, Outerwear_Closure_Type, Bottom_Closure_Type, Front_Style]
		attribute_name = None
		for attribute in attributes:
			for i in attribute.ATTRIBUTE_TYPE_CHOICES:
				if i[0] == attribute.attribute_type:
					"""if i[0] == 15:
						j = 13
					else:
						j = i[0]-1
					attribute_name = attribute_tables[j].objects.get(pk=attribute.attribute_id).name"""
					if i[0] == 1:
						attribute_name = Sweater_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 2:
						attribute_name = Jacket_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 3:
						attribute_name = Blazer_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 4:
						attribute_name = Sweatshirt_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 5:
						attribute_name = Jumpsuit_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 6:
						attribute_name = Style.objects.get(pk=attribute.attribute_id)
					elif i[0] == 7:
						attribute_name = Color.objects.get(pk=attribute.attribute_id)
					elif i[0] == 8:
						attribute_name = Pattern.objects.get(pk=attribute.attribute_id)
					elif i[0] == 9:
						attribute_name = Material.objects.get(pk=attribute.attribute_id)
					elif i[0] == 10:
						attribute_name = Silhouette.objects.get(pk=attribute.attribute_id)
					elif i[0] == 11:
						attribute_name = Outerwear_Structure.objects.get(pk=attribute.attribute_id)
					elif i[0] == 12:
						attribute_name = Pants_Structure.objects.get(pk=attribute.attribute_id)
					elif i[0] == 13:
						attribute_name = Decoration.objects.get(pk=attribute.attribute_id)
					elif i[0] == 14 or i[0] == 15:
						attribute_name = Neckline.objects.get(pk=attribute.attribute_id)
					elif i[0] == 16:
						attribute_name = Sleeve_Length.objects.get(pk=attribute.attribute_id)
					elif i[0] == 17:
						attribute_name = Sleeve_Style.objects.get(pk=attribute.attribute_id)
					elif i[0] == 18:
						attribute_name = Top_Length.objects.get(pk=attribute.attribute_id)
					elif i[0] == 19:
						attribute_name = Pants_Length.objects.get(pk=attribute.attribute_id)
					elif i[0] == 20:
						attribute_name = Shorts_Length.objects.get(pk=attribute.attribute_id)
					elif i[0] == 21:
						attribute_name = Skirt_Length.objects.get(pk=attribute.attribute_id)
					elif i[0] == 22:
						attribute_name = Fit_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 23:
						attribute_name = Waist_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 24:
						attribute_name = Top_Closure_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 25:
						attribute_name = Outerwear_Closure_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 26:
						attribute_name = Bottom_Closure_Type.objects.get(pk=attribute.attribute_id)
					elif i[0] == 27:
						attribute_name = Front_Style.objects.get(pk=attribute.attribute_id)
					attribute_set.append((i[1], attribute_name))

		#attribute_types = hasAttribute.ATTRIBUTE_TYPE_CHOICES
		return render(request, 'modifit/item.html', { 'item' : item, 'category' : category, 'attributes' : attribute_set })
	else:
		return HttpResponseRedirect('/')