# Generated by Django 3.1.3 on 2022-01-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartServices', '0004_auto_20220104_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='Address',
            field=models.CharField(default='Sangli', max_length=255),
        ),
        migrations.AlterField(
            model_name='partners',
            name='OtherExpertise',
            field=models.CharField(default='None', max_length=255),
        ),
    ]
