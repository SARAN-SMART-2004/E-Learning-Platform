# Generated by Django 5.0.6 on 2024-09-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0004_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="image",
            field=models.ImageField(blank=True, upload_to="course_images/"),
        ),
    ]
