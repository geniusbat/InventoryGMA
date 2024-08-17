from django.contrib import admin
from django.urls import path, re_path, include

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("add/", thingForm_view, name="thingForm"),
    path("delete/<int:id>", thing_delete, name="thingDelete"),
    path("category/", category_view, name="categoryView"),
    path("category/add/", category_create, name="categoryForm"),
    path("category/delete/<int:id>", category_delete, name="categoryDelete"),
    path("location/", location_view, name="locationView"),
    path("location/add/", location_create, name="locationForm"),
    path("location/delete/<int:id>", location_delete, name="locationDelete"),
    path("filter/", filterThings_view, name="filterThings"),
    re_path(r"(?P<what>category|thing|location)/(?P<id>.+)", UpdateForm, name="updateForm"),
]
