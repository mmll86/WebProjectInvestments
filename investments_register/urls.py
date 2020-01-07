from django.urls import path
from .views import index, shareholder_detail

urlpatterns = [
		path('', index),
		path('shareholder_detail/<str:slug>', shareholder_detail, name='shareholder_url'),
    ]