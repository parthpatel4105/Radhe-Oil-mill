from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact_number', 'subject', 'short_reason', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'contact_number', 'subject', 'reason']
    readonly_fields = ['created_at']

    @admin.display(description='Reason')
    def short_reason(self, obj):
        if len(obj.reason) > 60:
            return obj.reason[:60] + '…'
        return obj.reason
