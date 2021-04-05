from functools import update_wrapper

from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


def admin_view(view, cacheable=False):
    """
    Не дает пользователю, который не является персоналом, зайти на сайт
    """
    def inner(request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.is_staff:
            return redirect('/')
        return view(request, *args, **kwargs)

    if not cacheable:
        inner = never_cache(inner)

    if not getattr(view, 'csrf_exempt', False):
        inner = csrf_protect(inner)

    return update_wrapper(inner, view)
