from django.db import models


class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.IntegerField(blank=False)
    authorized = models.BooleanField()
