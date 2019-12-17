# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0003_lookitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookitem',
            name='fid',
            field=models.IntegerField(default=0),
        ),
    ]
