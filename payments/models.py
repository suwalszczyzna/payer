from django.db import models


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(ExpenseCategory, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField()