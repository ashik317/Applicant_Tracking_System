from django.urls import path

from companies.views import CompanyListCreateAPIView

urlpatterns = [
    path("list/create/", CompanyListCreateAPIView.as_view(), name="company-list-create"),
]
