from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("add/", thingForm_view, name="thingForm"),
    path("category/add/", categoryForm_view, name="categoryForm"),
    #path('blog/', include('blog.urls'))
]
