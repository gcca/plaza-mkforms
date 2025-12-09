from django.views.generic import CreateView, ListView

from .models import DocumentAA


class DocumentAAListView(ListView):
    model = DocumentAA
    template_name = "plaza_mkforms/documentaa/list.html"


class DocumentAACreateView(CreateView):
    model = DocumentAA
    fields = ["name", "amount", "quantity"]
    template_name = "plaza_mkforms/documentaa/create.html"
    success_url = "/documentaa/"
