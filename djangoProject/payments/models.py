from django.db import models

import djangoProject.invoices
from djangoProject import invoices


class Payment(models.Model):
    text = models.TextField()


def find_bigger_payment_for_invoice():
    model = djangoProject.invoices.models.Invoice
    return invoices.models.Invoice.objects.filter(amount__gt=0)
