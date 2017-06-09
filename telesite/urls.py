from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^help/', views.help1, name='help1'),
    url(r'^$', views.index, name='index'),

]