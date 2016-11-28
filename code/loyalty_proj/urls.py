from django.conf.urls import include, url
from django.contrib import admin
from loyalty_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.post_list, name='post_list'),
]