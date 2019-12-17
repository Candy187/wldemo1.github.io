# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furn',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50, default='0')),
                ('fprice', models.FloatField()),
                ('fcategory', models.CharField(max_length=20)),
                ('fnum', models.IntegerField()),
                ('fphoto', models.ImageField(upload_to='furnphoto')),
                ('fdescribe', models.CharField(max_length=500, default='无')),
            ],
            options={
                'db_table': 'Furn',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('rname', models.CharField(max_length=20, default='0')),
                ('raddress', models.CharField(max_length=50, default='0')),
                ('rphone', models.CharField(max_length=20, default='0')),
                ('pay', models.FloatField()),
                ('paystate', models.BooleanField(default=False)),
                ('order_time', models.CharField(max_length=50, default='0')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('o_oid', models.IntegerField(default=0)),
                ('o_fid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50, default='0')),
                ('price', models.FloatField(default=0.0)),
                ('category', models.CharField(max_length=20, default='其他')),
                ('num', models.IntegerField(default=0)),
                ('buynum', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, default='0')),
                ('telephone', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=60, unique=True, default='0')),
                ('password', models.CharField(max_length=20, default='0')),
                ('regist_time', models.CharField(max_length=50, default='0')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
