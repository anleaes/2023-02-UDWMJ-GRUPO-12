from django.urls import path
from . import views

app_name = 'artes'

urlpatterns = [
    path('', views.list_artes, name='list_artes'),
    path('adicionar/', views.add_arte, name='add_arte'),
    path('editar/<int:id_arte>/', views.edit_arte, name='edit_arte'),
    path('excluir/<int:id_arte>/', views.delete_arte, name='delete_arte'),
    path('<int:id_arte>/', views.view_arte, name='view_arte'),
    path('buscar/', views.search_arte, name='search_arte'),
]