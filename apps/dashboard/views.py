from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.documents.models import Document

def dashboard_view(request):

    return render(
        request,
        "dashboard/index.html"
    )
    return render(
        request,
        "dashboard/index.html",
        context
    )
@login_required
def dashboard(request):

    company = getattr(request.user, "company", None)

    documents = Document.objects.filter(
        company=company
    )

    context = {

        "company": company,

        "total_documents": documents.count(),

        "invoices":
        documents.filter(
            document_type="invoice"
        ).count(),

        "receipts":
        documents.filter(
            document_type="receipt"
        ).count(),

        "templates": 4,

        "recent_documents":
        documents.order_by(
            "-created_at"
        )[:5]

    }

    return render(
        request,
        "dashboard/index.html",
        context
    )