# Generated by Django 5.0.6 on 2024-12-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20, verbose_name='Name of the Service')),
                ('sdesc', models.CharField(max_length=20, verbose_name='Description of the Service')),
                ('simage', models.ImageField(upload_to='service_image')),
                ('sprice', models.IntegerField()),
            ],
        ),
    ]
