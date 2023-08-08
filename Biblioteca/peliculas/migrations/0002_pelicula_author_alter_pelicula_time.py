# Generated by Django 4.2.3 on 2023-08-08 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='time',
            field=models.FloatField(),
        ),
    ]
