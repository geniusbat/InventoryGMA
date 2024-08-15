from django.contrib import admin
from django.urls import path, re_path, include

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("add/", thingForm_view, name="thingForm"),
    path("category/add/", categoryForm_view, name="categoryForm"),
    path("location/add/", locationForm_view, name="locationForm"),
    path("filter/", filterThings_view, name="filterThings"),
    re_path(r"(?P<what>category|thing|location)/(?P<id>.+)", UpdateForm, name="updateForm"),
]
