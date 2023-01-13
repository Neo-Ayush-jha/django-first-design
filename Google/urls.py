from django.contrib import admin
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
