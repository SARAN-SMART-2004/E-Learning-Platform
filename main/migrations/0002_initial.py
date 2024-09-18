# Generated by Django 5.0.6 on 2024-09-07 07:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='travelplan',
            name='members',
            field=models.ManyToManyField(related_name='accepted_travel_plans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='travelplan',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_travel_plans', to=settings.AUTH_USER_MODEL),
        ),
    ]
