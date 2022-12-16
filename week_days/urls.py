from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('<int:sign_week>',views.choose_day_of_week_int ),
    path('<str:sign_week>',views.choose_day_of_week,name = 'todo_week-name' ),

]