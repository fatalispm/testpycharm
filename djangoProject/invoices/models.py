from django.db import models


class Invoice(models.Model):
    amount = models.IntegerField()
    payment = models.ForeignKey(to='payments.Payment', on_delete=models.CASCADE)
