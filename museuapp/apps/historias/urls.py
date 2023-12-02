from django.urls import path
from . import views

app_name = 'historias'

urlpatterns = [
    path('', views.list_historias, name='list_historias'),
    path('adicionar/', views.add_historia, name='add_historia'),
    path('editar/<int:id_historia>/', views.edit_historia, name='edit_historia'),
    path('excluir/<int:id_historia>/', views.delete_historia, name='delete_historia'),
]
