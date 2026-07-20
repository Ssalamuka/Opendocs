from django import forms 
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:

        model = Company

        fields = "__all__"

        exclude = ["owner"]

        widgets = {

            "name": forms.TextInput(

                attrs={

                    "class":"form-control"

                }

            ),

            "email": forms.EmailInput(

                attrs={

                    "class":"form-control"

                }

            ),

            "phone": forms.TextInput(

                attrs={

                    "class":"form-control"

                }

            ),

            "currency": forms.Select(

                attrs={

                    "class":"form-select"

                }

            ),

            "address": forms.Textarea(

                attrs={

                    "class":"form-control",

                    "rows":4

                }

            ),

            "tax_number": forms.TextInput(

                attrs={

                    "class":"form-control"

                }

            ),

            "footer": forms.Textarea(

                attrs={

                    "class":"form-control",

                    "rows":3

                }

            )

        }