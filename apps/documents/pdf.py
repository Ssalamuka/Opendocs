from django.template.loader import render_to_string

from weasyprint import HTML

from django.http import HttpResponse


def document_pdf(

        request,

        pk

):

    document = Document.objects.get(

        pk=pk

    )

    html = render_to_string(

        "pdf/document.html",

        {

            "document": document

        }

    )

    pdf = HTML(

        string=html

    ).write_pdf()

    response = HttpResponse(

        pdf,

        content_type="application/pdf"

    )

    response[

        "Content-Disposition"

    ] = (

        f'filename="{document.number}.pdf"'

    )

    return response