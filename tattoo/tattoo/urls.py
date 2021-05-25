import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .utils import e_handler404, e_handler500, e_handler403, e_handler400


urlpatterns = [
    path('tattoo-studio-admin-panel/', admin.site.urls, name='admin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include('mainapp.urls')),
    path('contact/', include('email_send.urls'), name='contact')
]

handler404 = e_handler404
handler500 = e_handler500
handler403 = e_handler403
handler400 = e_handler400

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
