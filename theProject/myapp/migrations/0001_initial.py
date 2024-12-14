# Generated by Django 5.0.6 on 2024-12-14 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20, verbose_name='Name of the Project')),
                ('pdesc', models.CharField(max_length=100, verbose_name='Description of the Project')),
                ('pimage', models.ImageField(upload_to='project_images')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
