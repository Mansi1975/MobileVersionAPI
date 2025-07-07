from django.contrib import admin
from .models import MobileVersion

@admin.register(MobileVersion)
class MobileVersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'expiry_date', 'created_at', 'updated_at')
