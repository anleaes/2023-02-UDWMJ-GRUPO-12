from django.urls import path
from . import views

app_name = 'valores'

urlpatterns = [
    path('', views.list_valores, name='list_valores'),
    path('adicionar/', views.add_valor, name='add_valor'),
    path('editar/<int:id_valor>/', views.edit_valor, name='edit_valor'),
    path('excluir/<int:id_valor>/', views.delete_valor, name='delete_valor'),
]
