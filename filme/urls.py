from django.urls import path
from .views import homepage, home_filmes

urlpatterns = [
    path('', homepage),
    path('filme/', home_filmes)
]
