from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'user_type',
        'is_active',
        'is_staff',
        'phone',
        'city',
        'state',
        'country',
        'zip_code',
        'address',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'email', 'first_name', 'last_name', 'phone', 'city', 'state', 'country'
    ]
    list_filter =  [
        'is_active',
        'is_staff',
        'is_superuser',
        'user_type',
        'groups',
        'user_permissions',
        'created_at',
        'updated_at',
    ]

    ordering = ['email']

    # Make these fields clickable to go to their edit page
    list_display_links = ['email', 'first_name', 'last_name']

    # Actions for bulk updates
    actions = ['make_users_active', 'make_users_inactive']

    # Action to activate selected users
    def make_users_active(self, request, queryset):
        queryset.update(is_active=True)

    make_users_active.short_description = "Activate selected users"

    # Action to deactivate selected users
    def make_users_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_users_inactive.short_description = "Deactivate selected users"
