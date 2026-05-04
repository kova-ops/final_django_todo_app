from django.urls import path
from .import views

urlpatterns = [
    path('', views.todoListView.as_view(), name='todo_list'),
    path('create/', views.todoCreateView.as_view(), name='todo_create'),
    path('delete/<int:pk>/', views.tododeleteView.as_view(), name='todo_delete'),
    path('toggle/<int:pk>/', views.toggle_todo, name='todo_toggle'),
]
