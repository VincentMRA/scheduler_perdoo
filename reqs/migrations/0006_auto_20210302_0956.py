# Generated by Django 3.1.7 on 2021-03-02 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reqs", "0005_auto_20210302_0953"),
    ]

    operations = [
        migrations.AlterField(
            model_name="req",
            name="exec_date",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 3, 2, 9, 56, 13, 915111)
            ),
        ),
    ]