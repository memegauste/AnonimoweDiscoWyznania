"""Admin file."""
# Django
from django.contrib import admin

# Local
from .models import Designate


@admin.site.register(Designate)
class DesignateAdmin(admin.ModelAdmin):
    """Designate admin file."""

    list_display = [
        'msg_id',
        'approved',
    ]
    search_fields = [
        'msg_id',
    ]
