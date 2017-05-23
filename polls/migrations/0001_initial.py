# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, error_messages={b'required': b'Please enter an name.'})),
                ('email', models.EmailField(max_length=70, unique=True, null=True, blank=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
