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
    path('export/', views.export, name='export'),  # {host}/api/export
    path('graph-construction/', views.graph_construction, name='graph_construction'),  # {host}/api/export
    path('graph-viewer/', views.graph_viewer, name='graph_viewer'),  # {host}/api/export
    path('tf-idf/', views.td_idf, name='tf_idf'),  # {host}/api/tf-idf
    path('join/', views.join, name='join'),  # {host}/api/tf-idf
]
