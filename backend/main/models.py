"""Models file."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Designate(models.Model):
    """Designate model (based on discord data)."""

    msg_id = models.CharField(_('Message ID'), max_length=255)
    approved = models.BooleanField(_('Is approved?'), default=False)

    def __str__(self):  # noqa: D102
        return f'Designate [{self.msg_id}]'

    class Meta:  # noqa: D106
        verbose_name = _('Designation')
        verbose_name_plural = _('Designations')
