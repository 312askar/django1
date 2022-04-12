from django.urls import path
from .views import *
urlpatterns = [
    path('', get_tour_list, name='tour_list'),
    path('tour/<int:pk>', get_tour_detail, name='tour_detail')
]
