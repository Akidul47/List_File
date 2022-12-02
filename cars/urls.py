from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.rental_review, name='rental_review'),
    #path('rental_review/', views.rental_update, name='rental_review'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('assignment_1/', views.asignment_1, name='asignment_1'),
    path('assignment_2/', views.asignment_2, name='asignment_2'),
    path('assignment_3/', views.asignment_3, name='asignment_3'),
]