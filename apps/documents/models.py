from django.db import models
from django.conf import settings


class Document(models.Model):

    DOCUMENT_TYPES = [
        ("invoice", "Invoice"),
        ("quotation", "Quotation"),
        ("receipt", "Receipt"),
        ("proforma_invoice", "Proforma Invoice"),
        ("purchase_order", "Purchase Order"),
        ("credit_note", "Credit Note"),
        ("delivery_note", "Delivery Note"),
    ]

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("sent", "Sent"),
        ("paid", "Paid"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE
    )

    doc_type = models.CharField(
        max_length=20,
        choices=DOCUMENT_TYPES
    )

    number = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    client_name = models.CharField(
    max_length=255,
    default="Unknown Client")
    
    doc_type = models.CharField(
    max_length=20,
    choices=DOCUMENT_TYPES,
    default="invoice")
    client_email = models.EmailField(blank=True, null=True)

    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    tax = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        # 🔥 PRODUCTION-GRADE NUMBERING (per document type)
        if not self.number:

            last = Document.objects.filter(
                doc_type=self.doc_type
            ).order_by("-id").first()

            next_id = 1 if not last else last.id + 1

            prefix = {
                "invoice": "INV",
                "quotation": "QUO",
                "receipt": "REC",
                "proforma_invoice": "PRO",
                "purchase_order": "PO",
                "credit_note": "CRN",
                "delivery_note": "DEL",
            }.get(self.doc_type, "DOC")

            self.number = f"{prefix}-{next_id:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number} - {self.client_name}"
    
class DocumentItem(models.Model):

    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="items"
    )

    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.description    