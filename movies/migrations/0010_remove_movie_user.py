# Generated by Django 4.1.7 on 2023-02-18 18:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0009_movie_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="user",
        ),
    ]
