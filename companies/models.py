from django.db import models

from common.enums import IndustryChoices, CompanySizeChoices, HiringStatusChoices, RemoteOptionChoices, \
    BenefitsOfferedChoices, LegalStatusChoices, DocumentTypeChoices
from common.models import CreatedAtUpdatedAtBaseModel


class Company(CreatedAtUpdatedAtBaseModel):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    industry = models.CharField(
        max_length=50,
        choices=IndustryChoices.choices,
        default=IndustryChoices.IT
    )
    company_size = models.CharField(
        max_length=50,
        choices=CompanySizeChoices.choices,
        null=True,
        blank=True
    )
    description = models.TextField(null=True, blank=True)
    website_url = models.URLField(unique=True, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=50, null=True, blank=True)
    hiring_status = models.CharField(
        max_length=20,
        choices=HiringStatusChoices.choices,
        null=True,
        blank=True
    )
    remote_option = models.CharField(
        max_length=20,
        choices=RemoteOptionChoices.choices,
        null=True,
        blank=True
    )
    benefits_offered = models.CharField(
        max_length=20,
        choices=BenefitsOfferedChoices.choices,
        null=True,
        blank=True
    )
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    tax_id = models.CharField(max_length=100, blank=True, null=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    legal_status = models.CharField(
        max_length=20,
        choices=LegalStatusChoices.choices,
        default=LegalStatusChoices.LLC,
    )

    def __str__(self):
        return f'{self.company_name}'

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departments")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CompanyLocation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="locations")
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.city}, {self.country}"


class CompanyDocument(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(
        max_length=100,
        choices=DocumentTypeChoices.choices,
        default=DocumentTypeChoices.TERMS_AND_CONDITIONS,
    )
    document = models.FileField(upload_to="company_documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_type} - {self.company.company_name}"

    def clean(self):
        if not self.document.name.endswith('.pdf', '.doc', '.docx'):
            raise ValueError("Only PDF and Word documents are allowed.")
