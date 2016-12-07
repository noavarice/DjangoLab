from django.conf.urls import url
import views

urlpatterns = [
    url(r'upload$', views.upload),
    url(r'uploaded/[0-9a-zA-Z]{8}$', views.succeed),
    url(r'download/[0-9a-zA-Z]{8}$', views.download)
]
