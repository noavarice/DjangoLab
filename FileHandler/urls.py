from django.conf.urls import url
from views import handle

urlpatterns = [
    url(r'^$', handle),
]
