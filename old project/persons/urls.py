# persons/urls.py

from django.urls import path
from .views import PersonViewSet

person_list = PersonViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

person_detail = PersonViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', person_list, name='person-list'),
    path('<int:pk>/', person_detail, name='person-detail'),
]
