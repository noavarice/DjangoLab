from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.handle),
    url(r'success$', views.succeed),
]
