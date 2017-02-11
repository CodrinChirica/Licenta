
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', include('licenta_gui.urls')),
    url(r'^admin/', admin.site.urls),
]
