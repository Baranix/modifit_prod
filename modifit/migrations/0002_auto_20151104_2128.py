# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modifit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='edited_on',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Last edited date'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.URLField(),
        ),
    ]
