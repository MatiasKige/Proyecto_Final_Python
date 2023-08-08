# Generated by Django 4.2.3 on 2023-08-08 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='time',
            field=models.FloatField(),
        ),
    ]
