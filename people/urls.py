from . import views
from django.urls import path

urlpatterns = [
    path('', views.poeople_names),
    path('people_detail', views.people_info),
]
