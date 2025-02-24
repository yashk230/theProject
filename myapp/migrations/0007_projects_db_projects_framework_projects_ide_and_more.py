# Generated by Django 5.1.4 on 2025-01-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_projects_pname_alter_services_sname'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='db',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Database Used'),
        ),
        migrations.AddField(
            model_name='projects',
            name='framework',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Framework Used'),
        ),
        migrations.AddField(
            model_name='projects',
            name='ide',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='IDE Used'),
        ),
        migrations.AddField(
            model_name='projects',
            name='language',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Language Used'),
        ),
        migrations.AddField(
            model_name='projects',
            name='userinterface',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='User Interface'),
        ),
        migrations.AddField(
            model_name='projects',
            name='webbrowser',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Web Browser'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='pdesc',
            field=models.TextField(verbose_name='Description of the Project'),
        ),
        migrations.AlterField(
            model_name='services',
            name='sdesc',
            field=models.TextField(verbose_name='Description of the Service'),
        ),
    ]
