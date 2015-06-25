# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hollaBack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='status_id',
            field=models.IntegerField(unique=True),
        ),
    ]
