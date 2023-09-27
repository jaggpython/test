from django.db import models

class studentDetails(models.Model):
    first_name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10)
    job = models.IntegerField()
    salary = models.IntegerField()