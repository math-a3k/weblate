# -*- coding: utf-8 -*-
# Generated by Django 2.2.1 on 2019-05-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("trans", "0027_auto_20190517_1125")]

    operations = [
        migrations.AddField(
            model_name="vote", name="value", field=models.SmallIntegerField(default=0)
        )
    ]
