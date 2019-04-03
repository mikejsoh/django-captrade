from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance_list, name='finance_list'),
    path('finance/<int:pk>', views.finance_detail, name='finance_detail'),
    path('finance/new/',views.finance_new, name='finance_new'),
    path('finance/<int:pk>/edit', views.finance_edit, name='finance_edit')
]