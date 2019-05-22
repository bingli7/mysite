from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'info', views.basic_info, name='info'),
    url(r'welcome', views.welcome, name='welcome'),
]
