"""Django admin configurations for the plaza_mkforms app.

This module defines the admin interfaces for the models in the plaza_mkforms app,
allowing administrators to manage DocumentAA and Setting instances through the Django
admin site.
"""

import django.contrib.admin

import plaza_mkforms.models


@django.contrib.admin.register(plaza_mkforms.models.DocumentAA)
class DocumentAAAdmin(django.contrib.admin.ModelAdmin):
    """Admin interface for the DocumentAA model.

    This class customizes the Django admin interface for the DocumentAA model, providing
    list display, search fields, filters, and ordering options to facilitate easy
    management of DocumentAA instances.
    """

    list_display = ["name", "amount", "quantity", "created_at"]
    search_fields = ["name"]
    list_filter = ["created_at"]
    ordering = ["-created_at"]


@django.contrib.admin.register(plaza_mkforms.models.Setting)
class SettingAdmin(django.contrib.admin.ModelAdmin):
    """Admin interface for the Setting model.

    This class customizes the Django admin interface for the Setting model, providing
    list display and search fields to allow administrators to view and search Setting
    instances efficiently.
    """

    list_display = ["name", "logo"]
    search_fields = ["name"]
