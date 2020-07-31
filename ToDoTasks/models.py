from django.db import models



class Tasks(models.Model):

    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title