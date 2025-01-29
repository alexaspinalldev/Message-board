from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Coffee, VendorAbout

# Register your models here.

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('product_ID', 'coffee_name', 'vendor', 'listing_approved', 'created_at', 'updated_at')
    search_fields = ['coffee_name', 'vendor__first_name']  # Adjusted for foreign key search
    list_filter = ('listing_approved', 'vendor__first_name')


# Extend the vendor table
class VendorExt(admin.StackedInline):
    model = VendorAbout
    can_delete = False
    verbose_name_plural = "Vendor About"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [VendorExt]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
