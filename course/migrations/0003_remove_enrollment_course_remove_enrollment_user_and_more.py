# Generated by Django 5.0.6 on 2024-09-16 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enrollment",
            name="course",
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="user",
        ),
        migrations.DeleteModel(
            name="Course",
        ),
        migrations.DeleteModel(
            name="Enrollment",
        ),
    ]
