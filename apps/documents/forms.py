from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document

        fields = [
            "doc_type",
            "client_name",
            "client_email",
            "due_date",
            "status",
        ]