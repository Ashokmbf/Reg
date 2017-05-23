# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20170322_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
