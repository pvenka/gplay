# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pstore', '0003_auto_20171008_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sterm', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='queryresult',
            name='sterm',
        ),
        migrations.AddField(
            model_name='query',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pstore.QueryResult'),
        ),
    ]