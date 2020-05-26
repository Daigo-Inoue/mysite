from django.urls import path
from . import views

name = 'base'

urlpatterns = [
    # path('', views.top, name='top'),
    path('', views.TopView.as_view(), name='top'),
]
