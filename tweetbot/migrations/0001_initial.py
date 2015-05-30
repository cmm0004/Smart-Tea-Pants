# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
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
                ('screen_name', models.CharField(max_length=50)),
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
    ]
