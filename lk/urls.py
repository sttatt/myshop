from django.conf.urls import url
from . import views

app_name = 'lk'
urlpatterns = [
    url(r'^$', views.lk, name='main'),
    url(r'orders/', views.orders, name='orders')
]

