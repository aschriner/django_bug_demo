from django.db import models
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class TaskMetadata(models.Model):
    task = models.OneToOneField(ContentType)
    fieldymcfields = models.CharField(max_length=3)


class Task(models.Model):
    blah = models.CharField(max_length=1)