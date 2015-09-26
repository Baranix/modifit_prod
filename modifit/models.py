from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.

class UserAvatar(models.Model):
	user = models.ForeignKey(User)
	shoulder = models.DecimalField(max_digits=4, decimal_places=1, default=15, null=True, blank=True)
	bust = models.DecimalField(max_digits=4, decimal_places=1, default=34, null=True, blank=True)
	waist = models.DecimalField(max_digits=4, decimal_places=1, default=24, null=True, blank=True)
	hips = models.DecimalField(max_digits=4, decimal_places=1, default=34, null=True, blank=True)
	#length = models.PositiveIntegerField(default=0)
	height = models.DecimalField(max_digits=4, decimal_places=1, default=68, null=True, blank=True)

	SKINTONE_CHOICES = (
		('W', "Warm"),
		('C', "Cool"),
		('O', "Olive"),
		('N', "Neutral"),
	)
	skintone = models.CharField(max_length=1, choices=SKINTONE_CHOICES)

class Brand(models.Model):
	brand_name = models.CharField(max_length=100, default="None")

	def __unicode__(self):
		return self.brand_name

class Item(models.Model):
	item_name = models.CharField(max_length=100)
	brand = models.ForeignKey(Brand, verbose_name="Brand")
	created_by = models.ForeignKey(User, related_name='created_by')
	created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
	edited_by = models.ForeignKey(User, related_name='edited_by', null=True, blank=True, verbose_name="Last edited by")
	edited_on = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Last edited date")
	published = models.BooleanField(default=False, verbose_name="Publish?")

	def __unicode__(self):
		return self.item_name

class hasSize(models.Model):
	item = models.ForeignKey(Item)
	SIZE_CHOICES = (
		("XXS", "Extra, Extra Small"),
		("XS", "Extra Small"),
		("S", "Small"),
		("M", "Medium"),
		("L", "Large"),
		("XL", "Extra Large"),
		("XXL", "Extra, Extra Large"),
		("One", "One Size Fits All"),
	)
	size = models.CharField(max_length=3, choices=SIZE_CHOICES)
	shoulder = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	bust = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	waist = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	hips = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	length = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)

	def __unicode__(self):
		return self.size

class hasColor(models.Model):
	item = models.ForeignKey(Item)
	color_name = models.CharField(max_length=50, null=True, blank=True)
	red = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
	green = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
	blue = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(255)])
	image = models.ImageField(upload_to='img/items')

	def __unicode__(self):
		if self.color_name != None:
			return self.color_name
		else:
			return "Default"

class Pattern(models.Model):
	pattern_name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.pattern_name

class hasPattern(models.Model):
	item = models.ForeignKey(Item)
	pattern = models.ForeignKey(Pattern)

class Material(models.Model):
	material_name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.material_name

class hasMaterial(models.Model):
	item = models.ForeignKey(Item)
	material = models.ForeignKey(Material)
	amount = models.DecimalField(
		max_digits=5,
		decimal_places=2,
		default=100.00,
		validators=[MinValueValidator(0), MaxValueValidator(100.00)],
		verbose_name="Amount / Percentage"
	)

class Category(models.Model):
	category_name = models.CharField(max_length=150, unique=True, verbose_name="Category")

	def __unicode__(self):
		return self.category_name

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

class SubCategory(models.Model):
	category = models.ForeignKey(Category)
	subcategory_name = models.CharField(max_length=150, unique=True, verbose_name="Subcategory")

	def __unicode__(self):
		return self.subcategory_name

class hasSubCategory(models.Model):
	item = models.ForeignKey(Item)
	subcategory = models.ForeignKey(SubCategory)

	def __unicode__(self):
		return "Subcategory"

class Wardrobe(models.Model):
	user = models.ForeignKey(User)
	item = models.ForeignKey(Item)
	times_used = models.PositiveIntegerField(default=0)