# Generated by Django 5.0.6 on 2024-07-30 08:16

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_productreview_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='instructions',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]