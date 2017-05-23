# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='gender',
            field=models.IntegerField(null=True, choices=[(1, b'male'), (2, b'female'), (3, b'others')]),
        ),
    ]
