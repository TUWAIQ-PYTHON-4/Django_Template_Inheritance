from django.template.defaulttags import url
from django.urls import path
from . import views


app_name = 'to_do_list_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about, name='about'),
]
