from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.IntegerField(default=0)
    # model ke parameter ko display karana ke liye

    def __str__(self):
        return "%s " % (self.title)
