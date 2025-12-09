"""Django models for the plaza_mkforms app.

This module defines the database models for the plaza_mkforms app, including DocumentAA
and Setting, with their fields and behaviors.
"""

import django.db.models


class DocumentAA(django.db.models.Model):
    """Model representing a DocumentAA entity.

    This model stores information about a document, including its name, amount,
    quantity, and creation timestamp. It is used to manage document-related data in the
    plaza_mkforms application.
    """

    name = django.db.models.CharField(max_length=100)
    amount = django.db.models.IntegerField()
    quantity = django.db.models.IntegerField()
    created_at = django.db.models.DateTimeField(auto_now_add=True)


class Setting(django.db.models.Model):
    """Model representing a Setting entity.

    This model stores configuration settings, such as a name and a compressed logo. It
    includes an index on the name field for efficient querying.
    """

    name = django.db.models.CharField(max_length=100)
    logo = django.db.models.BinaryField(null=True, editable=True)

    class Meta:
        indexes = [django.db.models.Index(fields=["name"])]

    def __str__(self) -> str:
        """Return a string representation of the Setting.

        This method provides a human-readable string for the Setting instance,
        using its name field.

        Returns:
            str: The name of the Setting.
        """
        return f"{self.name}"
