from rest_framework import serializers

from common.enums import BenefitsOfferedChoices
from companies.models import Company, Department, CompanyLocation, CompanyDocument


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "id",
            "company",
            "name",
            "department",
        ]

class CompanyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyLocation
        fields = [
            "id",
            "company",
            "city",
            "state",
            "country",
            "postal_code",
        ]

class CompanyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDocument
        fields = [
            "alias",
            "company",
            "document_type",
            "document",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]
        read_only_fields = [
            "alias",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by"
        ]

class CompanySerializer(serializers.ModelSerializer):
    benefits_offered = serializers.ListField(
        child=serializers.ChoiceField(choices=BenefitsOfferedChoices.choices),
        required=False,
        allow_empty=True,
        default=list,
    )
    class Meta:
        model = Company
        fields = [
            "alias",
            "company_name",
            "industry",
            "company_size",
            "description",
            "website_url",
            "location",
            "contact_email",
            "contact_phone",
            "hiring_status",
            "remote_option",
            "benefits_offered",
            "logo",
            "linkedin_url",
            "twitter_url",
            "facebook_url",
            "instagram_url",
            "youtube_url",
            "tax_id",
            "registration_number",
            "legal_status",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]
        read_only_fields = [
            "alias",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        ]