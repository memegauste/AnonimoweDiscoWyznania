"""Main views file."""
# Django
from django.http import JsonResponse
from django.views import View


class IndexView(View):
    """Report whether the backend is online."""

    def get(self, request, *args, **kwargs):  # noqa: D102
        return JsonResponse({'online': True})
