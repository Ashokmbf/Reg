# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_course_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='intrest',
            field=models.IntegerField(null=True, choices=[(1, b'Java'), (2, b'Python'), (3, b'Android')]),
        ),
    ]
