# Generated by Django 4.2.7 on 2023-12-03 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artes', '0002_arte_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='url',
            field=models.CharField(max_length=200, verbose_name='URL'),
        ),
    ]