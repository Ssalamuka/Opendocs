from datetime import datetime
import qrcode

from io import BytesIO

from django.core.files import File


def build_qr(

        document

):

    qr = qrcode.make(

        f"/documents/{document.pk}"

    )

    stream = BytesIO()

    qr.save(

        stream,

        "PNG"

    )

    document.qr_code.save(

        f"{document.number}.png",

        File(stream),

        save=False

    )


def generate_document_number(doc_type):

    prefix = {

        "invoice": "INV",

        "quotation": "QTN",

        "receipt": "RCT",

        "delivery_note": "DN",

        "purchase_order": "PO",

        "credit_note": "CN",

        "debit_note": "DB",

    }.get(

        doc_type,

        "DOC"

    )

    date = datetime.now().strftime(

        "%Y%m%d"

    )

    return f"{prefix}-{date}"