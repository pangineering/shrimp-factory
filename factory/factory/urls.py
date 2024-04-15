from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("customers/", include("customers.urls")),
    path("pending/", include("pending.urls")),
    path("admin/", admin.site.urls),
]