# Generated by Django 3.2.13 on 2022-12-05 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='note_notice',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='notice_note',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='notice_pet',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pet_notice',
            field=models.BooleanField(default=True),
        ),
    ]
