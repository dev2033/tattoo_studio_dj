from django.urls import path

from .views import ContactView, CustomerRecordView


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('customer-record/', CustomerRecordView.as_view(), name='customer_record')
]
