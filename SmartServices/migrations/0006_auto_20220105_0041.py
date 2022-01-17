# Generated by Django 3.1.3 on 2022-01-04 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SmartServices', '0005_auto_20220104_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partners',
            options={'ordering': ('-created',), 'verbose_name_plural': 'partner'},
        ),
        migrations.AlterField(
            model_name='partners',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Partner_maker', to=settings.AUTH_USER_MODEL),
        ),
    ]