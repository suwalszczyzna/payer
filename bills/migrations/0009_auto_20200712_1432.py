# Generated by Django 3.0.8 on 2020-07-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('bills', '0008_bill_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='expenses',
            field=models.ManyToManyField(blank=True, to='payments.Expense'),
        ),
    ]
