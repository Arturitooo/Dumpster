# Generated by Django 4.2.1 on 2023-06-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_app', '0004_remove_patient_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
