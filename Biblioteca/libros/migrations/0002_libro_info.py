# Generated by Django 4.2.3 on 2023-07-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='info',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]