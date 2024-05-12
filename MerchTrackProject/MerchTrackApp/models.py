from django.db import models

# Create your database models here.

class userInfo(models.Model):
    student_id = models.CharField(max_length=9)
    student_name = models.CharField(max_length=200)