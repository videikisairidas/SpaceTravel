# Generated by Django 5.0.6 on 2024-06-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0004_alter_stars_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='stars',
            name='myprompt',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
