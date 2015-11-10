# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modifit', '0004_auto_20151107_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_Closure_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='hasattribute',
            name='attribute_type',
            field=models.PositiveIntegerField(choices=[(1, b'Sweater Type'), (2, b'Jacket Type'), (3, b'Blazer Type'), (4, b'Sweatshirt Type'), (5, b'Jumpsuit Type'), (6, b'Style'), (7, b'Color'), (8, b'Pattern'), (9, b'Material'), (10, b'Silhouette'), (11, b'Outerwear Structure'), (12, b'Pants Structure'), (13, b'Decoration'), (14, b'Neckline'), (15, b'Collar'), (16, b'Sleeve Length'), (17, b'Sleeve Style'), (18, b'Top Length'), (19, b'Pants Length'), (20, b'Shorts Length'), (21, b'Skirt Length'), (22, b'Fit Type'), (23, b'Waist Type'), (24, b'Top Closure Type'), (25, b'Outerwear Closure Type'), (26, b'Bottom Closure Type'), (27, b'Front Style')]),
        ),
    ]
