from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.compress_view, name='upload'),
    path('api', include('analyze.api.urls')),
]
