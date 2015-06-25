# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hollaBack', '0002_auto_20150625_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsedtweet',
            name='polarity',
            field=models.DecimalField(max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='parsedtweet',
            name='subjectivity',
            field=models.DecimalField(max_digits=3, decimal_places=2),
        ),
    ]
