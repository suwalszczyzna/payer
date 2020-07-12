from django.contrib import admin
from .models import Currency, Bill, BillCategory

admin.site.register(Currency)
admin.site.register(BillCategory)
admin.site.register(Bill)
