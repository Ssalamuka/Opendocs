from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView
from apps.accounts.forms import LoginForm
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "dashboard/",
        include("apps.dashboard.urls")
    ),
    path("", include("apps.dashboard.urls")),
    path("documents/", include("apps.documents.urls")),
    path(
    "company/",
    include("apps.companies.urls")
   ),
   path("accounts/", include("django.contrib.auth.urls")),
   path(

'accounts/login/',

LoginView.as_view(

template_name='registration/login.html',

authentication_form=LoginForm

),

name='login'

),
path(

'accounts/logout/',

LogoutView.as_view(),

name='logout'

),
    
]