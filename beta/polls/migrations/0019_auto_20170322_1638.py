# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='addrID',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='cID',
        ),
    ]
