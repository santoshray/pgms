from django.conf.urls import url
from pgAccountApp import views


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^expense/$',views.expense,name="expense"),
    url(r'^managementTxn/$',views.managementTransaction,name="managementTransaction"),
    url(r'^tenantTxn/$',views.tenantTransaction,name="tenantTransaction"),
]
