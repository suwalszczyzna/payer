from django.db import models
from payments.models import Expense


class Currency(models.Model):
    name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BillCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Bill(models.Model):
    PLANNED = 1
    PAID = 2
    DELAYED = 3
    STATUS = (
        (PLANNED, 'Zaplanowany'),
        (PAID, 'Zapłacony'),
        (DELAYED, 'Po terminie'),
    )
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    category = models.ForeignKey(BillCategory, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    endless = models.BooleanField(default=False)
    payment_day = models.IntegerField(null=True, blank=True)
    expenses = models.ManyToManyField(Expense, blank=True)

    def __str__(self):
        return self.name
