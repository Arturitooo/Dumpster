# Generated by Django 4.2.1 on 2023-06-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_app', '0002_remove_patient_last_name_patient_heartrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
