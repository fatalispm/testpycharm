from django.db import models

from djangoProject.payments.models import Payment


class Invoice(models.Model):
    amount = models.IntegerField()
    payment = models.ForeignKey(to=Payment, on_delete=models.CASCADE)
