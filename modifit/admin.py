from django.contrib import admin

# Register your models here.

from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import uri_to_iri

from .models import Item, hasAttribute, hasCategory, Category

from .models import Style, Color, Pattern, Material, Decoration, Silhouette, Clothing_Length, Neckline, Collar, Sleeve_Length
from .models import Sleeve_Style, Sweater_Type, Jacket_Type, Blazer_Type, Sweatshirt_Type, Jumpsuit_Type, Outerwear_Structure
from .models import Pants_Structure, Top_Length, Pants_Length, Shorts_Length, Skirt_Length, Fit_Type, Waist_Type
from .models import Outerwear_Closure_Type, Bottom_Closure_Type, Front_Style

from .models import Wardrobe

"""class CategoryInline(admin.TabularInline):
	model = Category
	extra = 1
	verbose_name = "Category"
	verbose_name_plural = "Categories"""

class WardrobeAdmin(admin.ModelAdmin):
	list_display = ( 'user_id', 'item_id', 'rating' )

	list_filter = ( 'user_id__username', )


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)

class hasCategoryInline(admin.TabularInline):
	model = hasCategory
	extra = 1
	verbose_name = "Category"
	verbose_name_plural = "Categories"

class hasAttributeInline(admin.TabularInline):
	model = hasAttribute
	extra = 1
	verbose_name = "Attribute"
	verbose_name_plural = verbose_name + "s"

"""class hasStyleInline(admin.TabularInline):
	model = Style
	extra = 1
	verbose_name = "Style"
	verbose_name_plural = verbose_name + "s"

class hasPatternInline(admin.TabularInline):
	model = Pattern
	extra = 1
	verbose_name = "Pattern"
	verbose_name_plural = verbose_name + "s"

class hasMaterialInline(admin.TabularInline):
	model = Material
	extra = 1
	verbose_name = "Material"
	verbose_name_plural = verbose_name + "s"

class hasColorInline(admin.TabularInline):
	model = Color
	extra = 1
	verbose_name = "Color"
	verbose_name_plural = verbose_name + "s"

class hasDecorationInline(admin.TabularInline):
	model = Decoration
	extra = 1
	verbose_name = "Decoration"
	verbose_name_plural = verbose_name + "s"

class hasSilhouetteInline(admin.TabularInline):
	model = Silhouette
	extra = 1
	verbose_name = "Silhouette"
	verbose_name_plural = verbose_name + "s"""

class ItemAdmin(admin.ModelAdmin):
	inlines = [
		hasCategoryInline,
		hasAttributeInline
	]

	fieldsets = [
		(None, {'fields': ['name', 'published']}),
		("Image File", {'fields': ['image']})
	]
	
	list_display = ('thumbnail', 'name', 'category', 'edited', 'created', 'published',)

	list_filter = (
		'hascategory__category__name',
		'created_on',
		'published',
	)

	search_fields = [
		'name',
		'hascategory__category__name',
	]

	def thumbnail(self, obj):
		img = Item.objects.filter(id=obj.id)
		all_thumbs = ''
		for i in range(img.count()):
			url = uri_to_iri(img[i].image)
			all_thumbs = all_thumbs + '<img src="' + url + '" style="height:85px; width:auto;" />'
		return all_thumbs

	def edited(self, obj):
		return str(obj.edited_by) + "<br />" + obj.edited_on.strftime('%Y-%m-%d %H:%M:%S')

	def created(self, obj):
		return str(obj.created_by) + "<br />" + obj.created_on.strftime('%Y-%m-%d %H:%M:%S')

	def category(self, obj):
		hascat = hasCategory.objects.filter(item_id=obj.id)
		#subcat = SubCategory.objects.get(id=hassubcat.subcategory_id)
		cat = ""
		for cid in hascat:
			cat = cat + "<br />" + ( str( Category.objects.get(id=cid.category_id).__unicode__() ) )
		return cat[6:]

	# Allow HTML tags
	thumbnail.allow_tags = True
	edited.allow_tags = True
	created.allow_tags = True
	category.allow_tags = True

	# Allow Sortable columns
	#category.admin_order_field = 'hascategory__category'
	edited.admin_order_field = 'edited_on'
	created.admin_order_field = 'created_on'

	def save_model(self, request, obj, form, change):
		if change:
			obj.edited_by = request.user
			obj.edited_on = timezone.now()
		else:
			obj.created_by = request.user
			obj.created_on = timezone.now()
		obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Wardrobe, WardrobeAdmin)


"""	def subcategory(self, obj):
		hassubcat = hasSubCategory.objects.get(item_id=obj.id)
		subcat = SubCategory.objects.get(id=hassubcat.subcategory_id)
		return subcat"""