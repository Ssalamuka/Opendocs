from django.urls import path

from .views import (
    document_list,
    create_document,
    document_detail,
    delete_document,
    document_pdf,
)

urlpatterns = [
    path(
        "", 
        document_list, 
        name="documents"
    ),
    path(
        "create/", 
        create_document, 
        name="create_document"
    ),
    path(
        "<int:pk>/", 
        document_detail, 
        name="document_detail"
    ),
    path(
        "<int:pk>/delete/", 
        delete_document, 
        name="delete_document"
    ),
    path(
        "<int:pk>/pdf/", 
        document_pdf, 
        name="document_pdf"
    ),
]