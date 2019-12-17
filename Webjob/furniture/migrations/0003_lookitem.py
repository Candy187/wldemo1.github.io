# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0002_furn_fsale'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookItem',
            fields=[
                ('kid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('date', models.DateField(default='0')),
                ('lname', models.CharField(max_length=50, default='0')),
                ('lprice', models.FloatField(default=0.0)),
                ('lcategory', models.CharField(max_length=20, default='其他')),
            ],
            options={
                'db_table': 'LookItem',
            },
        ),
    ]
