# Generated by Django 4.2.6 on 2023-10-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('autor', models.CharField(max_length=120)),
                ('cantidad_paginas', models.IntegerField()),
            ],
        ),
    ]
