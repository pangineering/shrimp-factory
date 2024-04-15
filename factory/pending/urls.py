from django.urls import path

from . import views

urlpatterns = [
    path("", views.pending_index, name="pending_index"),
]