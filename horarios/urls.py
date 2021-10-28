from django.urls import path
from .views import CreateAgenda, ListAgenda, UpdateAgenda


urlpatterns = [
    path('create/', CreateAgenda.as_view(), name='create-agenda'),
    path('list/', ListAgenda.as_view(), name='list-agenda'),
    path('update/<int:pk>', UpdateAgenda.as_view(), name='update-agenda'),
]
