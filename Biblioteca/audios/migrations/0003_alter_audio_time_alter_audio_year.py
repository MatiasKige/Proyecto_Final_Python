# Generated by Django 4.2.3 on 2023-08-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0002_audio_year_alter_audio_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='audio',
            name='year',
            field=models.IntegerField(),
        ),
    ]