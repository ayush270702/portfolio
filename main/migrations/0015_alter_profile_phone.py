# Generated by Django 4.2.1 on 2023-07-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_alter_profile_about_me"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
