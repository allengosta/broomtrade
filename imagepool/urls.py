from django.conf.urls import url
from imagepool.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(get_list), name="imagepool_index"),
    url(r'^upload/$', login_required(upload_file), name="imagepool_upload"),
    url(r'^(?P<pk>\d+)/delete/$', login_required(delete_file), name="imagepool_delete"),
]