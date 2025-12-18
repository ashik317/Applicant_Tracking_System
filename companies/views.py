from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from companies.models import Company, CompanyDocument
from companies.serializers import (
    CompanySerializer,
    CompanyDocumentSerializer
)


#Create Company List Create api.
class CompanyListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = [
        "company_name",
        "contact_email",
        "contact_phone",
    ]
    search_fields = [
        "company_name",
        "contact_email",
        "contact_phone",
    ]
    ordering_fields = [
        "company_name",
        "contact_email",
        "contact_phone",
    ]
    ordering = ["company_name"]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Company Update Delete api.
class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = 'alias'

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

# Document List Create views.
class DocumentListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyDocumentSerializer

    def get_queryset(self):
        return CompanyDocument.objects.all().select_related('company')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Document Retrieve Update Delete api.
class DocumentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyDocumentSerializer
    lookup_field = 'alias'

    def get_queryset(self):
        return CompanyDocument.objects.filter(
            alias=self.kwargs['alias']
        ).select_related('company')

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

