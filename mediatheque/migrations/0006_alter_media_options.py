# Generated by Django 5.0.7 on 2024-10-07 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediatheque', '0005_alter_media_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['titre']},
        ),
    ]