from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import Contact, Client, Record
from .forms import ContactForm, ClientRecordForm
from .tasks import appointment_by_email, mailing_by_email
from tattoo.loguru_logger import logger


class ContactView(CreateView):
    """Отображение формы подписки по email"""
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'email_send/contacts.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        mailing_by_email.delay(form.instance.email)
        return super().form_valid(form)


class ClientRecordView(View):
    """Запись клиента на сеанс"""
    def get(self, request, *args, **kwargs):
        form = ClientRecordForm(request.POST or None)
        context = {'form': form}
        return render(request, 'email_send/customer_record.html', context)

    @logger.catch
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            form = ClientRecordForm(request.POST or None)
            client = Client.objects.get(user=request.user)
            if form.is_valid():
                new_record = form.save(commit=False)
                new_record.client = client
                new_record.email = form.cleaned_data['email']
                new_record.first_name = form.cleaned_data['first_name']
                new_record.last_name = form.cleaned_data['last_name']
                new_record.phone = form.cleaned_data['phone']
                new_record.message = form.cleaned_data['message']
                new_record.save()
                client.records.add(new_record)
                appointment_by_email.delay(new_record.email)
                return HttpResponseRedirect('/')
        except Exception as e:
            logger.error(f'Error! not client {e}')
            return HttpResponseRedirect('/')






