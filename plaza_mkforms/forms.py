"""Django forms for the plaza_mkforms app.

This module defines custom forms for handling user input related to the models in the
plaza_mkforms app, including form validation and saving logic.
"""

import lzma

import django.forms

import plaza_mkforms.models


class SettingForm(django.forms.ModelForm):
    """Form for creating and updating Setting instances.

    This form is based on the Setting model and includes a file field for the logo. It
    handles the compression of the logo data before saving to the database.
    """

    logo = django.forms.FileField(required=False)

    class Meta:
        model = plaza_mkforms.models.Setting
        fields = ["name", "logo"]

    def save(self, commit=True):
        """Save the form instance, compressing the logo if provided.

        This method overrides the default save behavior to compress the uploaded logo
        using LZMA compression with extreme preset before storing it in the database.
        If no logo is provided, it saves normally.

        Args:
            commit (bool): Whether to save the instance to the database immediately.
                           Defaults to True.

        Returns:
            Setting: The saved Setting instance.
        """
        instance = super().save(commit=False)
        if self.cleaned_data.get("logo"):
            data = self.cleaned_data["logo"].read()
            instance.logo = lzma.compress(data, preset=lzma.PRESET_EXTREME)
        if commit:
            instance.save()
        return instance
