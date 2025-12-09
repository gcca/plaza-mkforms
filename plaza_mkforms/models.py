import django.db.models


class DocumentAA(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)
    amount = django.db.models.IntegerField()
    quantity = django.db.models.IntegerField()
    created_at = django.db.models.DateTimeField(auto_now_add=True)


class Setting(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)
    logo = django.db.models.BinaryField(null=True)

    class Meta:
        indexes = [django.db.models.Index(fields=["name"])]

    def __str__(self) -> str:
        return f"{self.name}"
