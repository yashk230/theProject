# Generated by Django 5.1.4 on 2025-01-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_projects_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='pimage',
            field=models.ImageField(blank=True, null=True, upload_to='project_images'),
        ),
    ]
