# Generated by Django 4.2.1 on 2023-05-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_resume"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("type", models.CharField(blank=True, max_length=10, null=True)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("university", models.CharField(max_length=200, null=True)),
                ("city", models.CharField(blank=True, max_length=200, null=True)),
                ("course", models.CharField(max_length=200, null=True)),
                ("marks", models.IntegerField(null=True)),
            ],
        ),
    ]
