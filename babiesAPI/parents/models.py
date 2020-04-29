from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'id: {} parent name: {}'.format(self.pk, self.name)
    