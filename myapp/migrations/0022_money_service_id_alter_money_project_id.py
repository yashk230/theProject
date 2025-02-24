# Generated by Django 5.1.4 on 2025-01-14 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_money_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='service_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.services', verbose_name='Project ID'),
        ),
        migrations.AlterField(
            model_name='money',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.projects', verbose_name='Project ID'),
        ),
    ]
