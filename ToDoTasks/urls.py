from django.urls import path, include
from .views import *
urlpatterns = [
    path('task/', returnHomePage, name='task'),
    path('task/delete/<str:pk_>', deleteTask, name='delete_task'),
    path('task/update/<str:pk_>', updateTask, name='update_task')
]