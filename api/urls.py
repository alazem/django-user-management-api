from django.urls import path
from .views import user_delete, user_create, user_list

urlpatterns= [
    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('users/<int:user_id>/', user_delete, name='user_delete'),
]