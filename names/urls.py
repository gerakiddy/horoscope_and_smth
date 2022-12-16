from . import views
from django.urls import path,converters

urlpatterns = [
    path('', views.index,name='horoscope-index'),
    path('type', views.types_of_zodiack),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('type/<str:zodiac>', views.group_of_zodiack, name='type-name'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiace_int),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiace, name='horoscope-name'),
    # path('<randoming>',views.task_from_Artem),
    # path('<randoming>',views.get_guinness_world_records),

]
