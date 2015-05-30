# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetbot', '0004_auto_20150412_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hours_since_last_tweet',
            field=models.IntegerField(null=True),
        ),
    ]
