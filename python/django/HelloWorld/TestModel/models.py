from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField(null=True)

    def __unicode__(self):
        return self.name