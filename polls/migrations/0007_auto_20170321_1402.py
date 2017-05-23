# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170321_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='country',
            field=models.CharField(max_length=10, null=True, choices=[(b'India', b'India'), (b'Australia', b'Australia'), (b'America', b'America'), (b'Paris', b'Paris')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='gender',
            field=models.CharField(max_length=7, null=True, choices=[(b'male', b'male'), (b'female', b'female'), (b'others', b'others')]),
        ),
    ]
