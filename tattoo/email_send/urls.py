from django.urls import path

from .views import ContactView, ClientRecordView


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('customer-record/', ClientRecordView.as_view(), name='customer_record')
]
