from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance_list, name="finance_list"),
    path('finance/<int:pk>', views.finance_detail, name="finance_detail")
]