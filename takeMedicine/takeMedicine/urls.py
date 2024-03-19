from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/atualizar/<int:medicamento_id>/', views.atualizar_status_medicamento, name='atualizar_status_medicamento'),
    path('medicamentos/adicionar/', views.adicionar_medicamento, name='adicionar_medicamento'),
    path('medicamentos/remover/<int:medicamento_id>/', views.remover_medicamento, name='remover_medicamento'),
]
