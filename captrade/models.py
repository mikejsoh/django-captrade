from django.conf import settings
from django.db import models
from django.utils import timezone


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Finance(models.Model):
    finance_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    productionLevel = models.PositiveIntegerField()
    salesPrice = models.DecimalField(max_digits=20, decimal_places=2)
    unitCost = models.DecimalField(max_digits=20, decimal_places=2)
    totalProductionCost = models.DecimalField(max_digits=20, decimal_places=2)
    grossMargin = models.DecimalField(max_digits=20, decimal_places=2)
    fixedCost = models.DecimalField(max_digits=20, decimal_places=2)
    profit = models.DecimalField(max_digits=20, decimal_places=2)
