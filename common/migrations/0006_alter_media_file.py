# Generated by Django 5.0.6 on 2024-05-22 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_ourinstagramstory_story_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mp3', 'flac', 'doc', 'pdf'])], verbose_name='File'),
        ),
    ]
