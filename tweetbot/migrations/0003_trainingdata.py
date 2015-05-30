# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweetbot', '0002_user_classification'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingData',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('contributors_enabled', models.BooleanField()),
                ('hours_since_last_tweet', models.IntegerField()),
                ('declared_blogger', models.BooleanField()),
                ('declared_company', models.BooleanField()),
                ('num_entities', models.IntegerField()),
                ('tweets_favorited', models.IntegerField()),
                ('num_followers', models.IntegerField()),
                ('num_friends', models.IntegerField()),
                ('geo_enabled', models.BooleanField()),
                ('is_translator', models.BooleanField()),
                ('listed_count', models.IntegerField()),
                ('protected', models.BooleanField()),
                ('num_tweets', models.IntegerField()),
                ('has_profile_url', models.BooleanField()),
                ('verified', models.BooleanField()),
                ('classification', models.CharField(max_length=50, default='?')),
            ],
        ),
    ]
