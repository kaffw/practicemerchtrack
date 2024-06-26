# Generated by Django 5.0.6 on 2024-05-12 03:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MerchTrackApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='student_id',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[0-9]{1,9}$', 'Student ID must be numeric and have at most 9 digits.')]),
        ),
    ]
