# -*- coding: utf-8 -*-
# Generated by Django 2.2.5 on 2019-09-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("weblate_auth", "0005_auto_20190516_1153")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Mark user as inactive instead of removing.",
                verbose_name="Active",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="User has all possible permissions.",
                verbose_name="Superuser status",
            ),
        ),
    ]
