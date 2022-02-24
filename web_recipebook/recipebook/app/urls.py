from django.urls import path

from . import views


urlpatterns = [
        path('', views.home, name='index'),
        path('ingredient/<int:pk>/', views.ingredients_id_filter, name="recipes"),
        path('recipe/<int:pk>/', views.recipes_id_filter, name="recipes"),
        ]
