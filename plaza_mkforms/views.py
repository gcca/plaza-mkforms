import django.urls
import django.views.generic

import plaza_mkforms.models


class DocumentAAListView(django.views.generic.ListView):
    model = plaza_mkforms.models.DocumentAA
    template_name = "plaza_mkforms/documentaa/list.html"


class DocumentAACreateView(django.views.generic.CreateView):
    model = plaza_mkforms.models.DocumentAA
    fields = ["name", "amount", "quantity"]
    template_name = "plaza_mkforms/documentaa/create.html"
    success_url = django.urls.reverse_lazy("plaza-mkforms:documentaa-list")
