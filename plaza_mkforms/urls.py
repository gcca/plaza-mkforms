from django.urls import path

from . import views

app_name = "plaza-mkforms"

urlpatterns = [
    path(
        "documentaa/list/",
        views.DocumentAAListView.as_view(),
        name="documentaa-list",
    ),
    path(
        "documentaa/create/",
        views.DocumentAACreateView.as_view(),
        name="documentaa-create",
    ),
]
