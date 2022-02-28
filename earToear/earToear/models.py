from asyncio.windows_events import NULL
import numbers
from django.db import models

class JFLaughs (models.Model):
    Joke = models.CharField(max_length=200, null=True)
    Answer = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.Joke + '  ' + self.Answer

