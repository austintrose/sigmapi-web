# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PartyList', '0007_ever_signed_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='partyguest',
            name='wasVouchedFor',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]