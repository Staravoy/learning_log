# Визначає urls patterns для learning_logs
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),  # головна сторінка
    path('topics/', views.topics, name='topics'),  # сторінка з усіма темами
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # сторінка для окремої теми
    path('new_topic/', views.new_topic, name='new_topic'),  # сторінка для додавання нової теми
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),  # сторінка для додавання нового допису
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),  # сторінка редагування допису
]
