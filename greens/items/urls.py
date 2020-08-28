from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='items-home'),
    path('stock/',views.stock, name='items-stock'),
]