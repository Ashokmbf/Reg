# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_course_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='email',
            field=models.EmailField(max_length=70, unique=True, null=True),
        ),
    ]
