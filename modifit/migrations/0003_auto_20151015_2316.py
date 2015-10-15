# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modifit', '0002_auto_20150927_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wardrobe',
            old_name='times_used',
            new_name='rating',
        ),
    ]
