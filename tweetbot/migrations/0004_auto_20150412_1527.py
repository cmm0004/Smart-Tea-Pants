# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetbot', '0003_trainingdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingdata',
            name='hours_since_last_tweet',
            field=models.IntegerField(null=True),
        ),
    ]
