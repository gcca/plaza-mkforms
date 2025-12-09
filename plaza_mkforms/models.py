import django.db.models


class DocumentAA(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)
    amount = django.db.models.IntegerField()
    quantity = django.db.models.IntegerField()
