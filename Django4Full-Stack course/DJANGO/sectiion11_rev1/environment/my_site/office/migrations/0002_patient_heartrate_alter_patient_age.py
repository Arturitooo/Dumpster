# Generated by Django 4.2.1 on 2023-07-29 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='heartrate',
            field=models.IntegerField(default=60, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
