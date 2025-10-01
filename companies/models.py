from django.contrib.postgres.fields import ArrayField
from django.db import models

from common.enums import (
    IndustryChoices,
    CompanySizeChoices,
    HiringStatusChoices,
    RemoteOptionChoices,
    BenefitsOfferedChoices,
    LegalStatusChoices,
    DocumentTypeChoices
)
from common.models import CreatedAtUpdatedAtBaseModel
from django.core.exceptions import ValidationError



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
    website_url = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.PositiveIntegerField(null=True, blank=True, default=0)
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
    benefits_offered = ArrayField(
        base_field=models.CharField(
            max_length=50,
            choices=BenefitsOfferedChoices.choices,
        ),
        default=list,
        blank=True,
    )
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    tax_id = models.PositiveIntegerField(blank=True, null=True, default=0)
    registration_number = models.PositiveIntegerField(blank=True, null=True, default=0)
    legal_status = models.CharField(
        max_length=20,
        choices=LegalStatusChoices.choices,
        default=LegalStatusChoices.LLC,
    )

    def clean(self):
        if self.contact_phone and isinstance(self.contact_phone, str) and self.contact_phone.strip()=="":
            raise ValidationError({'contact_phone': 'Cannot be an empty string.'})
        if self.registration_number and isinstance(self.registration_number, str) and self.registration_number.strip()=="":
            raise ValidationError({'registration_number': 'Cannot be an empty string.'})
        if self.tax_id and isinstance(self.tax_id, str) and self.tax_id.strip()=="":
            raise ValidationError({'tax_id': 'Cannot be an empty string.'})

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


class CompanyDocument(CreatedAtUpdatedAtBaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(
        max_length=100,
        choices=DocumentTypeChoices.choices,
        default=DocumentTypeChoices.TERMS_AND_CONDITIONS,
    )
    document = models.FileField(upload_to="company_documents/")

    def __str__(self):
        return f"{self.document_type} - {self.company.company_name}"

    def clean(self):
        allowed = ('.pdf', '.doc', '.docx')
        if self.document and not self.document.name.lower().endswith(allowed):
            raise ValidationError("Only PDF and Word documents are allowed.")
