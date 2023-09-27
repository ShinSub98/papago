from django.urls import path
from . import views

app_name = 'translate'

urlpatterns = [
    path('trans/', views.translate),
    path('code/', views.code),
]