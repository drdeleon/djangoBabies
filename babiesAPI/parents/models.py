from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'parent name: {}'.format(self.name)
    