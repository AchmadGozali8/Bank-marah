# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=10)),
                ('deleted', models.IntegerField(choices=[(0, 'Not Deleted'), (1, 'Deleted')], default=0)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('deleted', models.IntegerField(choices=[(0, 'Not Deleted'), (1, 'Deleted')], default=0)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('anger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Anger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]