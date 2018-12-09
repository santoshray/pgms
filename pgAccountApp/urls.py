from django.conf.urls import url
from pgAccountApp import views


urlpatterns = [
    url(r'^$',views.index,name="index"),
]
