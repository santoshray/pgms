from django.conf.urls import url
from userAccountApp import views


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^register/$',views.register,name="register"),
    url(r'^edit/$',views.edit,name="edit"),
    url(r'^upload/$',views.upload,name="upload"),
    url(r'^residentlist/$',views.residentlist,name="residentlist"),

]
