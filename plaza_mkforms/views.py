import io

import django.http
import django.urls
import django.views.generic
import reportlab.lib.pagesizes
import reportlab.pdfgen.canvas

import plaza_mkforms.models


class DocumentAAListView(django.views.generic.ListView):
    model = plaza_mkforms.models.DocumentAA
    template_name = "plaza_mkforms/documentaa/list.html"


class DocumentAACreateView(django.views.generic.CreateView):
    model = plaza_mkforms.models.DocumentAA
    fields = ["name", "amount", "quantity"]
    template_name = "plaza_mkforms/documentaa/create.html"
    success_url = django.urls.reverse_lazy("plaza-mkforms:documentaa-list")


class DocumentAAEditView(django.views.generic.UpdateView):
    model = plaza_mkforms.models.DocumentAA
    fields = ["name", "amount", "quantity"]
    template_name = "plaza_mkforms/documentaa/edit.html"
    success_url = django.urls.reverse_lazy("plaza-mkforms:documentaa-list")


class PDFView(django.views.generic.DetailView):
    model = plaza_mkforms.models.DocumentAA

    def get(self, request, *args, **kwargs):
        document = self.get_object()
        response = django.http.HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = (
            f'inline; filename="{document.name}.pdf"'
        )
        buffer = io.BytesIO()
        p = reportlab.pdfgen.canvas.Canvas(
            buffer, pagesize=reportlab.lib.pagesizes.letter
        )
        p.drawString(100, 750, f"DocumentAA: {document.name}")
        p.drawString(100, 730, f"Amount: {document.amount}")
        p.drawString(100, 710, f"Quantity: {document.quantity}")
        p.showPage()
        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
