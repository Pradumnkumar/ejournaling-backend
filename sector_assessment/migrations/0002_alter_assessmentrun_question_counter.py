# Generated by Django 4.2.16 on 2024-11-13 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sector_assessment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentrun',
            name='question_counter',
            field=models.PositiveIntegerField(default=datetime.datetime(2024, 11, 13, 17, 13, 42, 273255, tzinfo=datetime.timezone.utc)),
        ),
    ]
