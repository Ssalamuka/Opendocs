from django.contrib import admin
from .models import Document, DocumentItem


class DocumentItemInline(admin.TabularInline):
    model = DocumentItem
    extra = 1


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "client_name",
        "doc_type",
        "status",
        "total"
    )

    inlines = [DocumentItemInline]