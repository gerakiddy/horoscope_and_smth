from . import views
from django.urls import path

urlpatterns = [
    path('<figure>',views.figurere),
    path('rectangle/<int:width>/<int:height>', views.rectangle,name='figure-r'),
    path('square/<int:width>', views.square,name='figure-s'),
    path('circle/<int:radius>', views.circle,name= 'figure-c'),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area),
    # path('get_square_area/<int:width>', views.get_square_area),
    # path('get_circle_area/<int:radius>', views.get_circle_area),
]
