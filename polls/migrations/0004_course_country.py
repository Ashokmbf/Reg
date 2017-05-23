# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_course_intrest'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='country',
            field=models.IntegerField(null=True, choices=[(1, b'India'), (2, b'Australia'), (3, b'America'), (3, b'Paris')]),
        ),
    ]
