from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'fullname', 'is_active', 'is_staff']  # Fields to display in the list view
    list_filter = ['is_active', 'is_staff']  # Filters in the admin sidebar
    search_fields = ['email', 'fullname']  # Searchable fields
    ordering = ['email']  # Default ordering by email
    filter_horizontal = []  # Remove 'groups' and 'user_permissions' if not needed

# Register the CustomUser model with the admin
admin.site.register(CustomUser, CustomUserAdmin)
from .models import HealthData

admin.site.register(HealthData)