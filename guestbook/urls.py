from django.conf.urls import url, include
from guestbook.views import *

urlpatterns = [
    url(r'^$',GuestbookView.as_view() ,name="guestbook")
]