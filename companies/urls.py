from django.urls import path
from companies.views import (
    CompanyListCreateAPIView,
    CompanyRetrieveUpdateDestroyAPIView,
    DocumentListCreateAPIView,
    DocumentRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path("company/list/", CompanyListCreateAPIView.as_view(), name="company-list-create"),
    path("company/list/<uuid:alias>/", CompanyRetrieveUpdateDestroyAPIView.as_view(), name="company-detail"),
    path("document/list/", DocumentListCreateAPIView.as_view(), name="document-list-create"),
    path("document/list/<uuid:alias>/", DocumentRetrieveUpdateDestroyAPIView.as_view(), name="document-detail"),
]
