from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_personas, name='listar_personas'),
    path('crear/', views.crear_persona, name='crear_persona'),
    path('actualizar/<str:id>/', views.actualizar_persona, name='actualizar_persona'),
    path('eliminar/<str:id>/', views.eliminar_persona, name='eliminar_persona'),
]
