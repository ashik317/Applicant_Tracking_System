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
