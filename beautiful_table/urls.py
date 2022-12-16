from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='beautiful_table-name')
]