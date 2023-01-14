from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Drive.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Home),
    path("view/",View),
    path("form/",Form),
    path("course/",Course),
    path("online/",Online)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
