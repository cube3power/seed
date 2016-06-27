# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluesky', '0004_auto_20160607_1158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cycle',
            options={'get_latest_by': 'created', 'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='propertystate',
            old_name='building_home_energy_saver_identifier',
            new_name='building_home_energy_score_identifier',
        ),
        migrations.AddField(
            model_name='propertystate',
            name='source_eui_weather_normalized',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertystate',
            name='year_ending',
            field=models.DateField(blank=True, null=True),
        ),
    ]