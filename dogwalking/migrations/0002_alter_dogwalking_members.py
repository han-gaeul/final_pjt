# Generated by Django 3.2.13 on 2022-12-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogwalking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogwalking',
            name='members',
            field=models.IntegerField(default=1, null=True),
        ),
    ]