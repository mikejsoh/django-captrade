from django.shortcuts import render, get_object_or_404, redirect
from .models import Finance
from .forms import FinanceForm


def finance_list(request):
    finances = Finance.objects.order_by('finance_id')
    return render(request, 'captrade/finance_list.html', {
        'finances': finances
    })


def finance_detail(request, pk):
    finance = get_object_or_404(Finance, pk=pk)
    return render(request, 'captrade/finance_detail.html', {
        'finance': finance
    })


def finance_new(request):
    if request.method == "POST":
        form = FinanceForm(request.POST)
        if form.is_valid():
            finance = form.save()
            return redirect('finance_detail', pk=finance.pk)
    else:
        form = FinanceForm()
    return render(request, 'captrade/finance_edit.html', {
        'form': form
    })

def finance_edit(request, pk):
    finance = get_object_or_404(Finance, pk=pk)
    if request.method == "POST":
        form = FinanceForm(request.POST, instance=finance)
        if form.is_valid():
            finance = form.save()
            return redirect('finance_detail', pk = finance.pk)
    else:
        form = FinanceForm(instance=finance)
    return render(request, 'captrade/finance_edit.html', {
        'form': form
    })
