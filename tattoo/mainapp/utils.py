from django.views.defaults import (
    page_not_found,
    permission_denied,
    server_error,
    bad_request
)


def e_handler404(request, exception):
    return page_not_found(request, exception, 'errors/404.html')


def e_handler403(request, exception):
    return permission_denied(request, exception, 'errors/403.html')


def e_handler500(request):
    return server_error(request, 'errors/500.html')


def e_handler400(request, exception):
    return bad_request(request, exception, 'errors/400.html')



