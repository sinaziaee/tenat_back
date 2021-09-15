from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_api, name='apis'),
    path('temp', views.temp, name='temp'),
    path('import/', views.upload),  # {host}/api/import
    path('tokenize/', views.tokenize, name='tokenizer'),  # {host}/api/tokenize
    path('normalize/', views.normalize, name='normalizer'),  # {host}/api/normalize
    path('stem/', views.stem, name='stemmer'),  # {host}/api/stem
    path('lemmatize/', views.lemmatize, name='lemmatizer'),  # {host}/api/lemmatize
    path('stop-word-removal/', views.remove_stop_word, name='stop-word-removal'),  # {host}/api/stop-word-removal
    path('doc-statistics/', views.doc_statistics, name='doc-statistics'),  # {host}/api/doc-statistics
    path('export/', views.export, name='export'),  # {host}/api/export,
    path('tf-idf/', views.tf_idf, name='tf-idf')   # {host}/api/tf-idf
]
