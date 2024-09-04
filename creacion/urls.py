from django.urls import path
from .views import *

urlpatterns = [
    path('crear', crear, name='crear'),
    path('', listar, name='listar')]