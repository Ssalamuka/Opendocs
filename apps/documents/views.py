from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentForm
from .models import Document


# Helper function (Make sure this exists or is imported from utils.py)
def generate_document_number(document_type):
    # TODO: Implement your actual numbering logic here
    import uuid

    return f"DOC-{uuid.uuid4().hex[:6].upper()}"


@login_required
def company_view(request):
    # TODO: Add logic for your company view here
    return render(request, "companies/company_detail.html")


def document_create(request):
    return render(request, "documents/create.html")


def document_list(request):
    documents = Document.objects.all().order_by("-created_at")
    return render(request, "documents/list.html", {"documents": documents})


def create_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.company = request.user.company
            document.number = generate_document_number(document.document_type)
            document.save()
            return redirect("documents")
    else:
        form = DocumentForm()

    return render(request, "documents/create.html", {"form": form})


def document_detail(request, pk):
    document = get_object_or_404(Document, id=pk)
    return render(request, "documents/detail.html", {"document": document})


def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        document.delete()
        return redirect("documents")
    return render(request, "documents/delete.html", {"document": document})


def document_pdf(request, pk):
    return HttpResponse(f"PDF view placeholder for document {pk}")