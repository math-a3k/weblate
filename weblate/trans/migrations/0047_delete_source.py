# -*- coding: utf-8 -*-
# Generated by Django 2.2.5 on 2019-11-04 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("screenshots", "0006_remove_screenshot_sources"),
        ("trans", "0046_source_strings"),
    ]

    operations = [migrations.DeleteModel(name="Source")]
