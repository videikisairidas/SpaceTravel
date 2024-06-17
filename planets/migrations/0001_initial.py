# Generated by Django 5.0.6 on 2024-06-14 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('planetID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planets.planets')),
            ],
        ),
    ]
