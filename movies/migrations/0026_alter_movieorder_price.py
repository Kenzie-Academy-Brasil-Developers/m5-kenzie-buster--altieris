# Generated by Django 4.1.7 on 2023-02-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0025_alter_movieorder_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movieorder",
            name="price",
            field=models.FloatField(max_length=8),
        ),
    ]
