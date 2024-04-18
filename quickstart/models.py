from django.db import models
from datetime import datetime


class Record(models.Model):
    uuid = models.CharField(primary_key=True, max_length=50)
    contents = models.TextField(default='', null=True, blank=True)
