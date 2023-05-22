# Generated by Django 4.2.1 on 2023-05-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_alter_resume_resume"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="about_me",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="projects",
            name="link",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="resume",
            name="resume",
            field=models.FileField(upload_to="resume"),
        ),
    ]