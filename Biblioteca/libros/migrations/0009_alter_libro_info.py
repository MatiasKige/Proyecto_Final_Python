# Generated by Django 4.2.3 on 2023-08-12 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0008_alter_libro_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='info',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
