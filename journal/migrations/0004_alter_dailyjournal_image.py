# Generated by Django 3.2.13 on 2022-12-12 23:23

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_alter_healthjournal_medicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyjournal',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/daily_journal/'),
        ),
    ]