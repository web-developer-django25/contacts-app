from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number', 'address')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-updated_at',)
