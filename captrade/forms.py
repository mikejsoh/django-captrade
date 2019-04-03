from django import forms
from .models import Finance


class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ('finance_id',
                  'company_id',
                  'year',
                  'productionLevel',
                  'salesPrice',
                  'unitCost',
                  'totalProductionCost',
                  'grossMargin',
                  'fixedCost',
                  'profit',)

