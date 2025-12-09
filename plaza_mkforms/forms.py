import lzma

import django.forms

import plaza_mkforms.models


class SettingForm(django.forms.ModelForm):
    logo = django.forms.FileField(required=False)

    class Meta:
        model = plaza_mkforms.models.Setting
        fields = ["name", "logo"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get("logo"):
            data = self.cleaned_data["logo"].read()
            instance.logo = lzma.compress(data, preset=lzma.PRESET_EXTREME)
        if commit:
            instance.save()
        return instance
