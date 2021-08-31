# Generated by Django 3.2.6 on 2021-08-19 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Selections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_name', models.CharField(max_length=200)),
                ('selection_choices', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('service_detailed', models.TextField()),
                ('service_duration', models.TimeField()),
                ('service_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_prefix', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(max_length=100)),
                ('customer_surname', models.CharField(max_length=200)),
                ('customer_phone_prefix', models.IntegerField(null=True)),
                ('customer_phone', models.IntegerField(null=True)),
                ('customer_email', models.EmailField(max_length=254)),
                ('service_cost', models.FloatField()),
                ('total_duration', models.IntegerField()),
                ('chosen_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Haircoot.service')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Haircoot.service')),
            ],
        ),
    ]
