# Generated by Django 5.0.3 on 2024-04-12 17:27

import accounts.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_useraddress_verifictionotp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,13}$')], verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,13}$')], verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='pin_code',
            field=models.CharField(max_length=60, verbose_name='Pin code'),
        ),
        migrations.AlterField(
            model_name='verifictionotp',
            name='code',
            field=models.IntegerField(validators=[accounts.utils.check_otp_code], verbose_name='Otp code'),
        ),
    ]