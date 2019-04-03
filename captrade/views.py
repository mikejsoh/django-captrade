from django.shortcuts import render, get_object_or_404
from .models import Finance

# Create your views here.
def finance_list(request):
    finances = Finance.objects.order_by('finance_id')
    return render(request, 'captrade/finance_list.html',{
        'finances': finances
    })

def finance_detail(request, pk):
    finance=get_object_or_404(Finance, pk=pk)
    return render(request, 'captrade/finance_detail.html', {
        'finance': finance
    })