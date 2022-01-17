# Generated by Django 3.1.3 on 2022-01-09 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SmartServices', '0008_auto_20220108_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='created_by',
            field=models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, related_name='Partner_maker', to=settings.AUTH_USER_MODEL),
        ),
    ]