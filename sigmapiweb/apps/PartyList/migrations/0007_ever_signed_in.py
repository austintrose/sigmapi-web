# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PartyList', '0006_change_on_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='girls_ever_signed_in',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='party',
            name='guys_ever_signed_in',
            field=models.IntegerField(default=0),
        ),
    ]
