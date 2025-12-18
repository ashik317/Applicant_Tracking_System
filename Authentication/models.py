from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.enums import UserRoleChoices, NameTitleChoices
from common.models import CreatedAtUpdatedAtBaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)

        if not password:
            raise ValueError('Password must be provided')

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, CreatedAtUpdatedAtBaseModel):
    email = models.EmailField(db_index=True, unique=True, null=False, default=None)
    phone = models.CharField(db_index=True, max_length=20, unique=False, blank=True, null=True, default=None)
    title = models.CharField(max_length=64, choices=NameTitleChoices.choices, default=NameTitleChoices.MR)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.ImageField(upload_to="user/profile", blank=True, null=True)
    nid = models.CharField(
        max_length=50,
        unique=True,
        default=None,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Nid No."),
        help_text=_("National ID No. Example: YYYYXXXXXXXXXXXXX")
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as active."),
    )
    user_type = models.CharField(
        max_length=100,
        choices=UserRoleChoices.choices,
        default=UserRoleChoices.CANDIDATE,
    )
    city = models.CharField(
        db_index=True, max_length=64, unique=False, null=True, blank=True, default=None
    )
    state = models.CharField(
        db_index=True, max_length=64, unique=False, null=True, blank=True, default=None
    )
    country = models.CharField(
        db_index=True, max_length=64, unique=False, null=True, blank=True, default=None
    )
    zip_code = models.CharField(
        db_index=True, max_length=64, unique=False, null=True, blank=True, default=None
    )
    address = models.CharField(
        db_index=True, max_length=255, unique=False, null=True, blank=True, default=None
    )
    groups = models.ManyToManyField(
        "auth.Group", related_name="organization_groups", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="organization_user_permissions", blank=True
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name} - {self.email}'
