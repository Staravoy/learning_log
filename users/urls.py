# Визначення регулярних виразів URL для блоку users
from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # Додати уставні URL auth (автентифікації)
    path('register/', views.register, name='register'),  # Сторінка реєстрації
    path('logout/', views.logout, name='logout'),  # Сторінка виходу з акаунту
]
