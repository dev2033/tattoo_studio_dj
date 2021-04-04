from django.views.generic import CreateView

from .models import Contact, Client
from .forms import ContactForm, ClientForm
from .service import send
from .tasks import mailing_by_email


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


class CustomerRecordView(CreateView):
    """Отображение формы записи клиента на сеанс(консультацию)"""
    model = Client
    form_class = ClientForm
    success_url = '/'
    template_name = 'email_send/customer_record.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        mailing_by_email.delay(form.instance.email)
        return super().form_valid(form)
