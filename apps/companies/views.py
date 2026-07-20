from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CompanyForm
from .models import Company


@login_required
def company_view(request):
    """
    Display and update the authenticated user's company profile.
    Creates a company automatically if one does not already exist.
    """

    company, created = Company.objects.get_or_create(
        owner=request.user,
        defaults={
            "name": f"{request.user.username}'s Company"
        }
    )

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company
        )

        if form.is_valid():

            company = form.save(commit=False)
            company.owner = request.user
            company.save()

            messages.success(
                request,
                "Company updated successfully."
            )

            return redirect("company")

    else:

        form = CompanyForm(instance=company)

    context = {
        "form": form,
        "company": company
    }

    return render(
        request,
        "companies/company.html",
        context
    )