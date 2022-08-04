# Generated by Django 4.0.6 on 2022-08-03 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_description', models.CharField(max_length=500)),
            ],
        ),
    ]
