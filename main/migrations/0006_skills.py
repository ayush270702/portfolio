# Generated by Django 4.2.1 on 2023-05-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_languages_alter_education_marks"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]