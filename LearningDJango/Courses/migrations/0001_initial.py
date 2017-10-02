# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Shortcut')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data Starting')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Images')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created in')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
            ],
        ),
    ]