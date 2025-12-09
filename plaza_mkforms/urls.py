"""URL patterns for the plaza_mkforms app.

This module defines the URL routing for the plaza_mkforms app, mapping URLs to their
corresponding views for handling DocumentAA and Setting resources.
"""

import django.urls

import plaza_mkforms.views

app_name = "plaza-mkforms"

urlpatterns = [
    django.urls.path(
        "documentaa/list/",
        plaza_mkforms.views.DocumentAAListView.as_view(),
        name="documentaa-list",
    ),
    django.urls.path(
        "documentaa/create/",
        plaza_mkforms.views.DocumentAACreateView.as_view(),
        name="documentaa-create",
    ),
    django.urls.path(
        "documentaa/<int:pk>/edit/",
        plaza_mkforms.views.DocumentAAEditView.as_view(),
        name="documentaa-edit",
    ),
    django.urls.path(
        "documentaa/<int:pk>/pdf/",
        plaza_mkforms.views.PDFView.as_view(),
        name="documentaa-pdf",
    ),
    django.urls.path(
        "setting/list/",
        plaza_mkforms.views.SettingListView.as_view(),
        name="setting-list",
    ),
    django.urls.path(
        "setting/<int:pk>/edit/",
        plaza_mkforms.views.SettingUpdateView.as_view(),
        name="setting-edit",
    ),
]
