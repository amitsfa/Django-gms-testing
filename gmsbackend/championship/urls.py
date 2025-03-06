from django.urls import path
from . import views

urlpatterns = [
    path('', views.championship_list, name='championship_list'),
    path('<int:pk>/', views.championship_detail, name='championship_detail'),
]