# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(default=b'None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(unique=True, max_length=150, verbose_name=b'Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='hasColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color_name', models.CharField(max_length=50, null=True, blank=True)),
                ('red', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255)])),
                ('green', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255)])),
                ('blue', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(255)])),
                ('image', models.ImageField(upload_to=b'img/items')),
            ],
        ),
        migrations.CreateModel(
            name='hasMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=100.0, verbose_name=b'Amount / Percentage', max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
        migrations.CreateModel(
            name='hasPattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='hasSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=3, choices=[(b'XXS', b'Extra, Extra Small'), (b'XS', b'Extra Small'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'Extra Large'), (b'XXL', b'Extra, Extra Large'), (b'One', b'One Size Fits All')])),
                ('shoulder', models.DecimalField(default=0, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('bust', models.DecimalField(default=0, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('waist', models.DecimalField(default=0, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('hips', models.DecimalField(default=0, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('length', models.DecimalField(default=0, null=True, max_digits=4, decimal_places=1, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='hasSubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name=b'Created date')),
                ('edited_on', models.DateTimeField(auto_now=True, verbose_name=b'Last edited date', null=True)),
                ('published', models.BooleanField(default=False, verbose_name=b'Publish?')),
                ('brand', models.ForeignKey(verbose_name=b'Brand', to='modifit.Brand')),
                ('created_by', models.ForeignKey(related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(related_name='edited_by', verbose_name=b'Last edited by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material_name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pattern_name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategory_name', models.CharField(unique=True, max_length=150, verbose_name=b'Subcategory')),
                ('category', models.ForeignKey(to='modifit.Category')),
            ],
        ),
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shoulder', models.DecimalField(default=15, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('bust', models.DecimalField(default=34, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('waist', models.DecimalField(default=24, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('hips', models.DecimalField(default=34, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('height', models.DecimalField(default=68, null=True, max_digits=4, decimal_places=1, blank=True)),
                ('skintone', models.CharField(max_length=1, choices=[(b'W', b'Warm'), (b'C', b'Cool'), (b'O', b'Olive'), (b'N', b'Neutral')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wardrobe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('times_used', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(to='modifit.Item')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hassubcategory',
            name='item',
            field=models.ForeignKey(to='modifit.Item'),
        ),
        migrations.AddField(
            model_name='hassubcategory',
            name='subcategory',
            field=models.ForeignKey(to='modifit.SubCategory'),
        ),
        migrations.AddField(
            model_name='hassize',
            name='item',
            field=models.ForeignKey(to='modifit.Item'),
        ),
        migrations.AddField(
            model_name='haspattern',
            name='item',
            field=models.ForeignKey(to='modifit.Item'),
        ),
        migrations.AddField(
            model_name='haspattern',
            name='pattern',
            field=models.ForeignKey(to='modifit.Pattern'),
        ),
        migrations.AddField(
            model_name='hasmaterial',
            name='item',
            field=models.ForeignKey(to='modifit.Item'),
        ),
        migrations.AddField(
            model_name='hasmaterial',
            name='material',
            field=models.ForeignKey(to='modifit.Material'),
        ),
        migrations.AddField(
            model_name='hascolor',
            name='item',
            field=models.ForeignKey(to='modifit.Item'),
        ),
    ]
