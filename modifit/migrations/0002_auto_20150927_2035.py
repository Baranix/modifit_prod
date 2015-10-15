# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modifit', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hasSubCategory',
            new_name='hasCategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='hascategory',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to='modifit.Category', null=True),
        ),
        migrations.AddField(
            model_name='hascategory',
            name='category',
            field=models.ForeignKey(default=1, to='modifit.Category'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
