"""Django mixins for the plaza_mkforms app.

This module provides reusable mixins for views in the plaza_mkforms app, particularly
for enforcing authentication and permissions.
"""

import django.contrib.auth.mixins
import django.core.exceptions


class MkFormsMixin(django.contrib.auth.mixins.AccessMixin):
    """Mixin to enforce authentication and required permissions for views.

    This mixin ensures that only authenticated users with the necessary permissions can
    access the views that inherit from it. It checks for a list of required permissions
    related to DocumentAA and Setting models.
    """

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
        """Dispatch the request, checking authentication and permissions.

        This method is called before the view's main logic and verifies that the user
        is authenticated and has all the required permissions. If not, it handles
        the lack of permission appropriately.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponse: The response from the view or a permission denied response.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not all(
            request.user.has_perm(perm) for perm in self.required_permissions
        ):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
