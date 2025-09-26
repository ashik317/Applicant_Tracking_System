from django.db import models
from django.utils.translation import gettext_lazy as _

class UserRoleChoices(models.TextChoices):
    CANDIDATE= 'CANDIDATE', _('Candidate')
    RECRUITER= 'RECRUITER', _('Recruiter')
    ADMIN = 'ADMIN', _('Admin')

class NameTitleChoices(models.TextChoices):
    MR = "MR", _("Mr.")
    MRS = "MRS", _("Mrs.")
    MS = "MS", _("Ms.")
    DR = "DR", _("Dr.")
    MISS = "MISS", _("Miss.")
    MADAM = "MADAM", _("Madam.")
    MAIDEN = "MAIDEN", _("Maiden.")
    PROFESSOR = "PROFESSOR", _("Professor.")
    DOCTOR = "DOCTOR", _("Doctor.")

class IndustryChoices(models.TextChoices):
    IT = 'IT', _('Information Technology')
    HEALTHCARE = 'Healthcare', _('Healthcare')
    EDUCATION = 'Education', _('Education')
    FINANCE = 'Finance', _('Finance')
    RETAIL = 'Retail', _('Retail')
    MANUFACTURING = 'Manufacturing', _('Manufacturing')
    CONSULTING = 'Consulting', _('Consulting')
    NONPROFIT = 'Nonprofit', _('Nonprofit')
    OTHER = 'Other', _('Other')

class CompanySizeChoices(models.TextChoices):
    ONE_TO_TEN = '1-10', _('1-10 Employees')
    ELEVEN_TO_FIFTY = '11-50', _('11-50 Employees')
    FIFTY_ONE_TO_TWO_HUNDRED = '51-200', _('51-200 Employees')
    TWO_HUNDRED_ONE_TO_FIVE_HUNDRED = '201-500', _('201-500 Employees')
    FIVE_HUNDRED_PLUS = '501+', _('500+ Employees')

class HiringStatusChoices(models.TextChoices):
    HIRING = 'hiring', _('Hiring')
    NOT_HIRING = 'not_hiring', _('Not Hiring')
    PAUSED = 'paused', _('Hiring Paused')

class RemoteOptionChoices(models.TextChoices):
    REMOTE = 'remote', _('Remote')
    HYBRID = 'hybrid', _('Hybrid')
    ONSITE = 'on_site', _('On-site')

class LegalStatusChoices(models.TextChoices):
    LLC = 'LLC', _('Limited Liability Company')
    CORPORATION = 'Corporation', _('Corporation')
    SOLE_PROPRIETORSHIP = 'Sole Proprietorship', _('Sole Proprietorship')
    PARTNERSHIP = 'Partnership', _('Partnership')
    NONPROFIT = 'Nonprofit', _('Nonprofit')
    OTHER = 'Other', _('Other')

class BenefitsOfferedChoices(models.TextChoices):
    HEALTHCARE = 'healthcare', _('Healthcare')
    PAID_TIME_OFF = 'paid_time_off', _('Paid Time Off')
    RETIREMENT_PLAN = 'retirement_plan', _('Retirement Plan')
    STOCK_OPTIONS = 'stock_options', _('Stock Options')
    GYM_MEMBERSHIP = 'gym_membership', _('Gym Membership')
    CHILD_CARE = 'child_care', _('Child Care')
    PAID_PARENTS_LEAVE = 'paid_parents_leave', _('Paid Parental Leave')
    OTHER = 'other', _('Other')

class DocumentTypeChoices(models.TextChoices):
    TERMS_AND_CONDITIONS = 'terms_and_conditions', _('Terms and Conditions')
    OTHER = 'other', _('Other')
    PRIVACY = 'privacy', _('Privacy')
