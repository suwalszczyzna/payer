from django.contrib import admin

from payments.models import Expense, ExpenseCategory

admin.site.register(Expense)
admin.site.register(ExpenseCategory)
