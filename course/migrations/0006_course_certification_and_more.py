# Generated by Django 5.0.6 on 2024-09-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0005_course_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="certification",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="course",
            name="certification_description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="course",
            name="language",
            field=models.TextField(blank=True),
        ),
    ]
