# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20170321_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='intrest',
            field=models.CharField(max_length=10, null=True, choices=[(b'Java', b'Java'), (b'Python', b'Python'), (b'Android', b'Android')]),
        ),
    ]
