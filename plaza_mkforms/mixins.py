import django.contrib.auth.mixins
import django.core.exceptions


class MkFormsMixin(django.contrib.auth.mixins.AccessMixin):
    required_permissions = [
        "plaza_mkforms.add_documentaa",
        "plaza_mkforms.change_documentaa",
        "plaza_mkforms.delete_documentaa",
        "plaza_mkforms.view_documentaa",
        "plaza_mkforms.add_setting",
        "plaza_mkforms.change_setting",
        "plaza_mkforms.delete_setting",
        "plaza_mkforms.view_setting",
    ]

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not all(
            request.user.has_perm(perm) for perm in self.required_permissions
        ):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
