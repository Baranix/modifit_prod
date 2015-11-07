# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modifit', '0002_auto_20151104_2128'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clothing_Length',
        ),
        migrations.DeleteModel(
            name='Collar',
        ),
        migrations.AlterField(
            model_name='hasattribute',
            name='attribute_type',
            field=models.PositiveIntegerField(choices=[(1, b'Sweater Type'), (2, b'Jacket Type'), (3, b'Blazer Type'), (4, b'Sweatshirt Type'), (5, b'Jumpsuit Type'), (6, b'Style'), (7, b'Color'), (8, b'Pattern'), (9, b'Material'), (10, b'Silhouette'), (11, b'Outerwear Structure'), (12, b'Pants Structure'), (13, b'Decoration'), (14, b'Neckline'), (15, b'Sleeve Length'), (16, b'Sleeve Style'), (17, b'Top Length'), (18, b'Pants Length'), (19, b'Shorts Length'), (20, b'Skirt Length'), (21, b'Fit Type'), (22, b'Waist Type'), (23, b'Outerwear Closure Type'), (24, b'Bottom Closure Type'), (25, b'Front Style')]),
        ),
    ]
