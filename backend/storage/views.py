"""Main views file."""
from django.http import JsonResponse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):  # noqa: D102
        return JsonResponse({'online': True})
