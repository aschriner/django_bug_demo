from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from models import Task, TaskMetadata


def some_utility_function():
    task = Task
    ctype = ContentType.objects.get_for_model(task)
    try:
        ctype.taskmetadata
    except TaskMetadata.DoesNotExist:
        TaskMetadata.objects.get_or_create(task=ctype,
                                           fieldymcfields="123")
        print "Created TaskMetadata object for %s" % task.__name__
    else:
        print "TaskMetadata object already exists for %s" % task.__name__
        print ctype.taskmetadata
        print "ALL OF THEM!! %s" % TaskMetadata.objects.all()


class SimpleTest(TestCase):
    """One of these tests throws an error, and the other does not."""
    def setUp(self):
        some_utility_function()

    def test_something(self):
        ContentType.objects.get(taskmetadata__fieldymcfields="123")

    def test_something_again(self):
        ContentType.objects.get(taskmetadata__fieldymcfields="123")
