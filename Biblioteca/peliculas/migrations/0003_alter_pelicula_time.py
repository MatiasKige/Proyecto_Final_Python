# Generated by Django 4.2.3 on 2023-08-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_pelicula_author_alter_pelicula_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='time',
            field=models.IntegerField(),
        ),
    ]
