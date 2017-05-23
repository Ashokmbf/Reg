# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20170322_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='intrest',
            field=models.CharField(max_length=50, null=True, choices=[(b'1', b'Java'), (b'2', b'Python'), (b'3', b'Android')]),
        ),
    ]
