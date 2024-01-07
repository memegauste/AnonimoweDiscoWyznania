"""Models file."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Designate(models.Model):
    """Designate model (based on discord data)."""

    message = models.CharField(_('Message'), max_length=255)
    approved = models.BooleanField(_('Is approved?'), default=False)
    objects = models.Manager()

    def __str__(self):  # noqa: D102
        return f'Designate [{self.id}]'

    class Meta:  # noqa: D106
        verbose_name = _('Designation')
        verbose_name_plural = _('Designations')
