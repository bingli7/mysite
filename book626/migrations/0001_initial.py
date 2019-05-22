# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('M', 'Man'), ('F', 'Woman')], max_length=20)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
