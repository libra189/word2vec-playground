from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.word2vec, name='w2v'),
]