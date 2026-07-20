from weasyprint import HTML


def export_pdf(

        template,

        context

):

    return HTML(

        string=template

    ).write_pdf()