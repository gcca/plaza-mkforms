import django.contrib.admin

import plaza_mkforms.models


@django.contrib.admin.register(plaza_mkforms.models.DocumentAA)
class DocumentAAAdmin(django.contrib.admin.ModelAdmin):
    list_display = ["name", "amount", "quantity", "created_at"]
    search_fields = ["name"]
    list_filter = ["created_at"]
    ordering = ["-created_at"]


@django.contrib.admin.register(plaza_mkforms.models.Setting)
class SettingAdmin(django.contrib.admin.ModelAdmin):
    list_display = ["name", "logo"]
    search_fields = ["name"]
