# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20170321_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='country',
            field=models.IntegerField(null=True, choices=[(1, b'India'), (2, b'Australia'), (3, b'America'), (3, b'Paris')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='gender',
            field=models.IntegerField(null=True, choices=[(1, b'male'), (2, b'female'), (3, b'others')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='intrest',
            field=models.IntegerField(null=True, choices=[(1, b'Java'), (2, b'Python'), (3, b'Android')]),
        ),
    ]
