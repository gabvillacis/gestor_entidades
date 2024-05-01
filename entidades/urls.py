from django.urls import path
from entidades import views

urlpatterns = [
    path('', views.home),
    path('provincias/<int:provincia_id>/cantones/', views.get_cantones),
    path('cantones/<int:canton_id>/parroquias/', views.get_parroquias),
]