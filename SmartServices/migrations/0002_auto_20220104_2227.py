# Generated by Django 3.1.3 on 2022-01-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartServices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
