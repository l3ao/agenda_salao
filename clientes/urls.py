from django.urls import path
from .views import CreateCliente, ListCliente, UpdateCliente


urlpatterns = [
    path('create/', CreateCliente.as_view(), name='create-cliente'),
    path('list/', ListCliente.as_view(), name='list-cliente'),
    path('update/<int:pk>', UpdateCliente.as_view(), name='update-cliente'),
]
