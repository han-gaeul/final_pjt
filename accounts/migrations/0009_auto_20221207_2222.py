# Generated by Django 3.2.13 on 2022-12-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_authphone_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authphone',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='authphone',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authphone',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authphone',
            name='auth_number',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='authphone',
            table=None,
        ),
    ]