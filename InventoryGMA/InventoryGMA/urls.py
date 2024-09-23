from django.contrib import admin
from django.urls import path, re_path, include
from os import getenv
from django.conf import settings
from django.conf.urls.static import static

from .views import *


if getenv('MGMA_PREFIX_DOMAIN', "False") == "True":
    urlpatterns = [
        path("inventorygma/admin/", admin.site.urls),
        path("inventorygma/", index, name="index"),
        path("inventorygma/add/", thingForm_view, name="thingForm"),
        path("inventorygma/delete/<int:id>", thing_delete, name="thingDelete"),
        path("inventorygma/category/", category_view, name="categoryView"),
        path("inventorygma/category/add/", category_create, name="categoryForm"),
        path("inventorygma/category/delete/<int:id>", category_delete, name="categoryDelete"),
        path("inventorygma/location/", location_view, name="locationView"),
        path("inventorygma/location/add/", location_create, name="locationForm"),
        path("inventorygma/location/delete/<int:id>", location_delete, name="locationDelete"),
        path("inventorygma/filter/", filterThings_view, name="filterThings"),
        re_path(r"inventorygma/(?P<what>category|thing|location)/(?P<id>.+)", UpdateForm, name="updateForm"),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
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
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)