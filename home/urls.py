from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_index, name='show_index')
    ]
