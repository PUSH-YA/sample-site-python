# Generated by Django 5.0.1 on 2024-02-26 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_twitter',
        ),
    ]
