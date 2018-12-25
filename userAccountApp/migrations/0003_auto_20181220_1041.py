# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-12-20 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAccountApp', '0002_personalinforecord_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccountrecord',
            name='companyInfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companyInfo', to='userAccountApp.CompanyInfoRecord'),
        ),
        migrations.AddField(
            model_name='useraccountrecord',
            name='emergencyContactInfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emergencyContactInfo', to='userAccountApp.EmergencyContactRecord'),
        ),
        migrations.AddField(
            model_name='useraccountrecord',
            name='idVerificationInfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idVerification', to='userAccountApp.IdVerificationRecord'),
        ),
    ]