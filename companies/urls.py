from django.urls import path

from companies.views import (
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("company/list/", CompanyListCreateAPIView.as_view(), name="company-list-create"),
    path("company/list/<uuid:alias>/", CompanyRetrieveUpdateDestroyAPIView.as_view(), name="company-detail"),
]
