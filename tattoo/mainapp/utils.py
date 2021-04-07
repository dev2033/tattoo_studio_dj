from django.views.defaults import (
    page_not_found,
    permission_denied,
    server_error,
    bad_request
)


def e_handler404(request, exception):
    """Возвращает шаблон с 404 ошибкой"""
    return page_not_found(request, exception, 'errors/404.html')


def e_handler403(request, exception):
    """Возвращает шаблон с 403 ошибкой"""
    return permission_denied(request, exception, 'errors/403.html')


def e_handler500(request):
    """Возвращает шаблон с 500 ошибкой"""
    return server_error(request, 'errors/500.html')


def e_handler400(request, exception):
    """Возвращает шаблон с 400 ошибкой"""
    return bad_request(request, exception, 'errors/400.html')



