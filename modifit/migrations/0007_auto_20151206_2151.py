# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modifit', '0006_item_similarity_user_recommendations_user_similarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_recommendations',
            name='user_rating',
            field=models.IntegerField(default=0),
        ),
    ]
