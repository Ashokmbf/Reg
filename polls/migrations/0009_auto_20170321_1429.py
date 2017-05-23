# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20170321_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='country',
            field=models.IntegerField(null=True, choices=[(1, b'India'), (2, b'Australia'), (3, b'America'), (4, b'Paris')]),
        ),
    ]
