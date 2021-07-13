from django.urls import path

from . import views

# Nota: Si quieren ver la página web en su navegador deben de poner lo siguiente:
# http://127.0.0.1:8000/home/nombre_de_la_url/  
# Por ejemplo:
# http://127.0.0.1:8000/home/aes/  


urlpatterns = [
    #path('nombre_de_la_url', views.nombre_vista.as_view(), name='nombre_de_la_url'),
    path('aes/', views.AES_EBC.as_view(), name='aes'),
]