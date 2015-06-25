# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetbot', '0006_add_tea_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedTweet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('polarity', models.FloatField()),
                ('subjectivity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=140)),
                ('status_id', models.IntegerField()),
                ('user', models.ForeignKey(to='tweetbot.User')),
            ],
        ),
        migrations.AddField(
            model_name='parsedtweet',
            name='tweet',
            field=models.ForeignKey(to='hollaBack.Tweet'),
        ),
    ]
