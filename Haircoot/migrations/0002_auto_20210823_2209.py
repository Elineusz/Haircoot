# Generated by Django 3.2.6 on 2021-08-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Haircoot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='total_duration',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_duration',
            field=models.DurationField(),
        ),
    ]
