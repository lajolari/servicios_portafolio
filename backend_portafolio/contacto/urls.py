from django.urls import path
from contacto import views

urlpatterns = [
    path('mensajes/', views.mensaje_list),
    path('mensajes/<int:pk>/', views.mensaje_detail),
]