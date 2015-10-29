from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.

"""class UserAvatar(models.Model):
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
	skintone = models.CharField(max_length=1, choices=SKINTONE_CHOICES)"""

class Item(models.Model):
	name = models.CharField(max_length=250)
	image = models.ImageField(upload_to='img/items')
	created_by = models.ForeignKey(User, related_name='created_by')
	created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
	edited_by = models.ForeignKey(User, related_name='edited_by', null=True, blank=True, verbose_name="Last edited by")
	edited_on = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Last edited date")
	published = models.BooleanField(default=False, verbose_name="Publish?")

	def __unicode__(self):
		return self.name

class Category(models.Model):
	#parent = models.ForeignKey('self', null=True, blank=True)
	name = models.CharField(max_length=150, unique=True, verbose_name="Category")

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

class hasCategory(models.Model):
	item = models.ForeignKey(Item)
	category = models.ForeignKey(Category)

	def __unicode__(self):
		return "Category"

class hasAttribute(models.Model):
	ATTRIBUTE_TYPE_CHOICES = (
		(1, "Style"),
		(2, "Color"),
		(3, "Pattern"),
		(4, "Material"),
		(5, "Decoration"),
		(6, "Silhouette"),
		(7, "Clothing Length"),
		(8, "Neckline"),
		(9, "Collar"),
		(10, "Sleeve Length"),
		(11, "Sleeve Style"),
		(12, "Sweater Type"),
		(13, "Jacket Type"),
		(14, "Blazer Type"),
		(15, "Sweatshirt Type"),
		(16, "Jumpsuit Type"),
		(17, "Outerwear Structure"),
		(18, "Pants Structure"),
		(19, "Top Length"),
		(20, "Pants Length"),
		(21, "Shorts Length"),
		(22, "Skirt Length"),
		(23, "Fit Type"),
		(24, "Waist Type"),
		(25, "Outerwear Closure Type"),
		(26, "Bottom Closure Type"),
		(27, "Front Style"),
	)

	item = models.ForeignKey(Item)
	attribute_type = models.PositiveIntegerField(choices=ATTRIBUTE_TYPE_CHOICES)
	attribute_id = models.PositiveIntegerField()

	def __unicode__(self):
		return "Attribute: " + str(self.item)


#-------------------------------------------- Attribute Types ----------------------------------------------

class Style(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Color(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class Pattern(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Material(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Decoration(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Silhouette(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Clothing_Length(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Neckline(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Collar(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Sleeve_Length(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Sleeve_Style(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Sweater_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Jacket_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Blazer_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Sweatshirt_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Jumpsuit_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Outerwear_Structure(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Pants_Structure(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Top_Length(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Pants_Length(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Shorts_Length(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Skirt_Length(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Fit_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Waist_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Outerwear_Closure_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Bottom_Closure_Type(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

class Front_Style(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __unicode__(self):
		return self.name

#----------------------------------------------------- Wardrobe -------------------------------------------------


class Wardrobe(models.Model):
	user = models.ForeignKey(User)
	item = models.ForeignKey(Item)
	rating = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return str(self.user) + "'s " + str(self.item)