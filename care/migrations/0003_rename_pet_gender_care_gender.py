# Generated by Django 3.2.13 on 2022-12-07 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0002_auto_20221207_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='care',
            old_name='pet_gender',
            new_name='gender',
        ),
    ]