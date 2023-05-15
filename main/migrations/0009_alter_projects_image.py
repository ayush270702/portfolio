# Generated by Django 4.2.1 on 2023-05-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0008_contact_alter_projects_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/project",
                verbose_name="image(300x400)",
            ),
        ),
    ]