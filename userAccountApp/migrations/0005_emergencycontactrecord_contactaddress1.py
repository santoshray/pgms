# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-12-21 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAccountApp', '0004_useraccountrecord_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencycontactrecord',
            name='contactAddress1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emergencyAddress2', to='userAccountApp.AddressRecord'),
        ),
    ]