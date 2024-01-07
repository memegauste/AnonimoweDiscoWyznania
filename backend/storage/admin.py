"""Admin file."""
# Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# 3rd-party
import requests

# Local
from .models import Designate


@admin.action(description=_('Potwierdź zaznaczone wyznania'))
def generate_so_report_action(modeladmin, request, queryset):
    id_list = queryset.filter(approved=False).values_list('id', flat=True)
    if id_list:
        requests.post(
            'http://localhost:2137/handle-msg/',
            data={'msg_ids': list(id_list)},
        )



@admin.register(Designate)
class DesignateAdmin(admin.ModelAdmin):
    """Designate admin file."""

    list_display = [
        'id',
        'approved',
    ]
    search_fields = [
        'message',
    ]
    actions = [
        generate_so_report_action,
    ]
