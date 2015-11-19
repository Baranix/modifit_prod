# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modifit', '0005_auto_20151110_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Similarity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.DecimalField(default=0, max_digits=10, decimal_places=5)),
                ('item_1', models.ForeignKey(related_name='item_1', to='modifit.Item')),
                ('item_2', models.ForeignKey(related_name='item_2', to='modifit.Item')),
            ],
        ),
        migrations.CreateModel(
            name='User_Recommendations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projected_rating', models.DecimalField(default=0, max_digits=10, decimal_places=5)),
                ('user_rating', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(to='modifit.Item')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Similarity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.DecimalField(default=0, max_digits=10, decimal_places=5)),
                ('user_1', models.ForeignKey(related_name='user_1', to=settings.AUTH_USER_MODEL)),
                ('user_2', models.ForeignKey(related_name='user_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
