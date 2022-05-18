from django.urls import path, include
from .views import CreateCliente, ListCliente, UpdateCliente, DeleteCliente


urlpatterns = [
    path('create/', CreateCliente.as_view(), name='create-cliente'),
    path('list/', ListCliente.as_view(), name='list-cliente'),
    path('update/<int:pk>', UpdateCliente.as_view(), name='update-cliente'),
    path('delete/<int:pk>', DeleteCliente.as_view(), name='delete-cliente'),
]
