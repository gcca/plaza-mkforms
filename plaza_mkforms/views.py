"""Django views for the plaza_mkforms app.

This module contains class-based views for handling HTTP requests related to DocumentAA
and Setting models, including listing, creating, editing, and generating PDFs.
"""

import io

import django.http
import django.urls
import django.views.generic
import reportlab.lib.pagesizes
import reportlab.pdfgen.canvas

import plaza_mkforms.forms
import plaza_mkforms.mixins
import plaza_mkforms.models


class DocumentAAListView(
    plaza_mkforms.mixins.MkFormsMixin, django.views.generic.ListView
):
    """View for listing DocumentAA instances.

    This view displays a list of all DocumentAA objects, requiring authentication and
    specific permissions as enforced by the MkFormsMixin.
    """

    model = plaza_mkforms.models.DocumentAA
    template_name = "plaza_mkforms/documentaa/list.html"


class DocumentAACreateView(
    plaza_mkforms.mixins.MkFormsMixin, django.views.generic.CreateView
):
    """View for creating new DocumentAA instances.

    This view provides a form for creating new DocumentAA objects and redirects to the
    list view upon success. It requires authentication and permissions.
    """

    model = plaza_mkforms.models.DocumentAA
    fields = ["name", "amount", "quantity"]
    template_name = "plaza_mkforms/documentaa/create.html"
    success_url = django.urls.reverse_lazy("plaza-mkforms:documentaa-list")


class DocumentAAEditView(
    plaza_mkforms.mixins.MkFormsMixin, django.views.generic.UpdateView
):
    """View for editing existing DocumentAA instances.

    This view allows editing of DocumentAA objects via a form and redirects to the list
    view after saving. Authentication and permissions are required.
    """

    model = plaza_mkforms.models.DocumentAA
    fields = ["name", "amount", "quantity"]
    template_name = "plaza_mkforms/documentaa/edit.html"
    success_url = django.urls.reverse_lazy("plaza-mkforms:documentaa-list")


class PDFView(
    plaza_mkforms.mixins.MkFormsMixin, django.views.generic.DetailView
):
    """View for generating PDF for a DocumentAA instance.

    This view generates a PDF document containing details of a specific DocumentAA
    instance and returns it as an HTTP response. It requires authentication and
    permissions.
    """

    model = plaza_mkforms.models.DocumentAA

    def get(self, request, *args, **kwargs):
        """Handle GET request to generate and return a PDF.

        This method retrieves the DocumentAA instance, creates a PDF using ReportLab,
        and returns it as an inline response. The PDF includes the document's name,
        amount, and quantity.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments, including 'pk' for the object ID.

        Returns:
            HttpResponse: An HTTP response containing the generated PDF.
        """
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


class SettingListView(
    plaza_mkforms.mixins.MkFormsMixin, django.views.generic.ListView
):
    """View for listing Setting instances.

    This view displays a list of all Setting objects, requiring authentication and
    specific permissions as enforced by the MkFormsMixin.
    """

    model = plaza_mkforms.models.Setting
    template_name = "plaza_mkforms/setting/list.html"


class SettingUpdateView(
    plaza_mkforms.mixins.MkFormsMixin, django.views.generic.UpdateView
):
    """View for updating Setting instances.

    This view provides a form for updating Setting objects and redirects to the list
    view upon success. It requires authentication and permissions.
    """

    model = plaza_mkforms.models.Setting
    form_class = plaza_mkforms.forms.SettingForm
    template_name = "plaza_mkforms/setting/edit.html"
    success_url = django.urls.reverse_lazy("plaza-mkforms:setting-list")
