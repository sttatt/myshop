from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'index', views.index, name="index"),
    url(r'products', views.products, name="products"),
    url(r'registration', views.registration, name="registration"),
    url(r'logout', views.logout, name="logout"),
    url(r'auth', views.auth, name="auth"),
    url(r'omag', views.about, name="about"),
    url(r'cont', views.contacts, name="contacts"),


]
