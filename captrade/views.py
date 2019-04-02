from django.shortcuts import render

# Create your views here.
def finance_list(request):
    return render(request, 'captrade/finance_list.html',{})