from django.conf.urls import url
from django.contrib import admin

from personal_handle.views import DefaultView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', DefaultView.as_view(), name="default")
]
