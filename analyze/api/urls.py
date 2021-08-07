from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_api, name='apis'),
    path('temp', views.temp, name='temp'),
    # path('import', views.Upload.as_view()),
    path('import/', views.upload),  # {host}/api/import
    path('tokenize', views.tokenize),  # {host}/api/tokenize
]
