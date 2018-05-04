from django.conf.urls import url, include
from news.views import *
from django.contrib.auth.decorators import permission_required

urlpatterns =[
    url(r'^$', NewListView.as_view(), name="news_index"),
    url(r'^(?P<pk>\d+)/$', NewDetailView.as_view(), name="news_detail"),

    url(r'^add/$', permission_required("news.add_new")(NewCreate.as_view()), name="news_add"),
    url(r'^(?P<pk>\d+)/edit/$', permission_required("news.change_new")(NewUpdate.as_view()), name="news_edit"),
    url(r'^(?P<pk>\d+)/delete/$', permission_required("news.delete_new")(NewDelete.as_view()), name="news_delete"),

]