# Generated by Django 5.0.3 on 2024-03-18 11:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='ClientModel',
        ),
        migrations.RenameModel(
            old_name='Project',
            new_name='ProjectModel',
        ),
    ]
