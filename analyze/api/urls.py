from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_api, name='apis'),
    path('temp', views.temp, name='temp'),
    path('import/', views.upload),  # {host}/api/import
    path('tokenize/', views.tokenize, name='tokenizer'),  # {host}/api/tokenize
    path('normalize/', views.normalize, name='normalizer'),  # {host}/api/normalize
    path('stem/', views.stem, name='stemmer'),  # {host}/api/stem
]
