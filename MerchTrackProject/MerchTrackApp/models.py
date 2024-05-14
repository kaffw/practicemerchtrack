from django.db import models
from django.core.validators import RegexValidator

# Create your database models here.

class userInfo(models.Model):
    student_id = models.CharField(max_length=9, validators=[RegexValidator(r'^[0-9]{1,9}$', 'Student ID must be numeric and have at most 9 digits.')])
    student_name = models.CharField(max_length=200)

# class order_info(models.Model):
