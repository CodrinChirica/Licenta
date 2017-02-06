from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rank/$', views.googleRankChecker, name='googleRankChecker'),
]
