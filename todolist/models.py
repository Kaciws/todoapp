from django.db import models


class Todo(models.Model):
    added_date = models.DateTimeField()
    text_input = models.CharField(max_length=200)
# Create your models here.
