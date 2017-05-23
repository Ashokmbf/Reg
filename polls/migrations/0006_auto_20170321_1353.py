# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170321_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='country',
            field=models.IntegerField(null=True, choices=[(1, b'India'), (2, b'Australia'), (3, b'America'), (4, b'Paris')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='intrest',
            field=models.CharField(max_length=7, null=True, choices=[(b'Java', b'Java'), (b'Python', b'Python'), (b'Android', b'Android')]),
        ),
    ]
