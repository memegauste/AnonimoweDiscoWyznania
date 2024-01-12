"""Admin file."""
from django.conf import settings
# Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# 3rd-party
import requests

# Local
from .models import Designate


@admin.action(description=_('Confirm selected designations'))
def confirm_designations(modeladmin, request, queryset):
    id_list = queryset.filter(approved=False).values_list('id', flat=True)
    if id_list:
        requests.post(
            'http://host.docker.internal:2137/handle-msg/',
            json={
                'token': getattr(settings, 'DISCORD_MSG_TOKEN', None),
                'msg_ids': list(id_list),
            },
        )


@admin.register(Designate)
class DesignateAdmin(admin.ModelAdmin):
    """Designate admin file."""

    list_display = [
        'message',
        'approved',
        'created_dt',
    ]
    search_fields = [
        'message',
    ]
    actions = [
        confirm_designations,
    ]
