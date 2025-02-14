from django.contrib import admin
from django.urls import path, include, re_path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^courses/', include('courses.urls')),
    re_path(r'^', include('accounts.urls')),
    re_path(r'^suggest/$', views.suggestion_view, name='suggestion'),
    re_path(r'^$', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
