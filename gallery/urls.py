from django.urls import path
from .views import *

urlpatterns = [

    path('notice/<int:pk>/',CollectNotice,name='collect_notice')
]