from django.http import JsonResponse
from django.shortcuts import render

from djangoProject.payments.models import find_bigger_payment_for_invoice


def my_view(request):
    response = find_bigger_payment_for_invoice()
    return JsonResponse({'response': 'Hello World'})
