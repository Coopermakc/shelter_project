# Generated by Django 2.2.13 on 2020-09-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=1),
        ),
    ]
