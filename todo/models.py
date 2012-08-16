from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_new_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
