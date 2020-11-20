from django.db import models

class TimeStampModel(models.Model):

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']