from django.contrib import admin

# Register your models here.

from django.utils import timezone

from django.contrib.auth.models import User

from .models import Item, hasSize, hasColor
from .models import Category, SubCategory, hasSubCategory
from .models import Pattern, hasPattern
from .models import Material, hasMaterial
from .models import Brand

class SubCategoryInline(admin.TabularInline):
	model = SubCategory
	extra = 1
	verbose_name = "Subcategory"
	verbose_name_plural = "Subcategories"

class CategoryAdmin(admin.ModelAdmin):
	inlines = [SubCategoryInline]

class hasSubCategoryInline(admin.TabularInline):
	model = hasSubCategory
	extra = 1
	verbose_name = "Subcategory"
	verbose_name_plural = "Subcategories"

class hasPatternInline(admin.TabularInline):
	model = hasPattern
	extra = 1
	verbose_name = "Pattern"
	verbose_name_plural = "Patterns"

class hasMaterialInline(admin.TabularInline):
	model = hasMaterial
	extra = 1
	verbose_name = "Material"
	verbose_name_plural = "Materials"

class hasSizeInline(admin.TabularInline):
	model = hasSize
	extra = 1
	verbose_name = "Size"
	verbose_name_plural = "Sizes"

class hasColorInline(admin.TabularInline):
	model = hasColor
	extra = 1
	verbose_name = "Color"
	verbose_name_plural = "Colors"

class ItemAdmin(admin.ModelAdmin):
	inlines = [
		hasSubCategoryInline,
		hasSizeInline,
		hasColorInline,
		hasPatternInline, 
		hasMaterialInline
	]

	fieldsets = [
		(None, {'fields': ['item_name', 'brand', 'published']}),
	]
	
	list_display = ('thumbnail', 'item_name', 'category', 'subcategory', 'brand', 'edited', 'created', 'published')

	list_filter = (
		'hassubcategory__subcategory__category__category_name',
		'hassubcategory__subcategory__subcategory_name',
		'brand',
		'created_on',
		'published',
	)

	search_fields = [
		'item_name',
		'hassubcategory__subcategory__category__category_name',
		'hassubcategory__subcategory__subcategory_name',
	]

	def thumbnail(self, obj):
		color = hasColor.objects.filter(item_id=obj.id)
		all_thumbs = ''
		for i in range(color.count()):
			all_thumbs = all_thumbs + '<img src="' + color[i].image.url + '" style="height:85px; width:auto;" />'
		return all_thumbs

	def edited(self, obj):
		return str(obj.edited_by) + "<br />" + obj.edited_on.strftime('%Y-%m-%d %H:%M:%S')

	def created(self, obj):
		return str(obj.created_by) + "<br />" + obj.created_on.strftime('%Y-%m-%d %H:%M:%S')

	# Allow HTML tags
	thumbnail.allow_tags = True
	edited.allow_tags = True
	created.allow_tags = True

	def subcategory(self, obj):
		hassubcat = hasSubCategory.objects.get(item_id=obj.id)
		subcat = SubCategory.objects.get(id=hassubcat.subcategory_id)
		return subcat

	def category(self, obj):
		hassubcat = hasSubCategory.objects.get(item_id=obj.id)
		subcat = SubCategory.objects.get(id=hassubcat.subcategory_id)
		cat = Category.objects.get(id=subcat.category_id)
		return cat

	# Allow Sortable columns
	subcategory.admin_order_field = 'hassubcategory__subcategory'
	category.admin_order_field = 'hassubcategory__subcategory__category'
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
admin.site.register(Pattern)
admin.site.register(Material)
admin.site.register(Brand)