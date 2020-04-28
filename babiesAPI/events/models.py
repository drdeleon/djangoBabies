from django.db import models

class Event(models.Model):
    event_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField( (""), auto_now=False, auto_now_add=False)
    baby = models.ForeignKey("babies.Baby", on_delete=models.SET_NULL, null = True, blank=True)

    def __str__(self):
        return 'event: {} | baby: {}'.format(self.event_type, self.baby)
