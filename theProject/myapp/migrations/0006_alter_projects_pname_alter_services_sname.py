# Generated by Django 5.1.4 on 2024-12-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='pname',
            field=models.CharField(max_length=50, verbose_name='Name of the Project'),
        ),
        migrations.AlterField(
            model_name='services',
            name='sname',
            field=models.CharField(max_length=50, verbose_name='Name of the Service'),
        ),
    ]
