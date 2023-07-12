import requests
from django.conf import settings
from django.views.generic import FormView
from django.contrib import messages
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/contact/success/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        try:
            subject = 'Contact Form Submission'
            recipient_list = ['mk.moukangwe@gmail.com']
            self.send_email_via_mailgun(subject, message, email, recipient_list)

            messages.success(self.request, 'Thank you for contacting me! I will get back to you soon.')
        except Exception as e:
            messages.error(self.request, 'An error occurred. Please try again later.')

        return super().form_valid(form)

    def send_email_via_mailgun(self, subject, message, sender_email, recipient_list):
        api_key = settings.MAILGUN_API_KEY
        domain = settings.MAILGUN_DOMAIN
        url = f'https://api.mailgun.net/v3/{domain}/messages'

        data = {
            'from': sender_email,
            'to': recipient_list,
            'subject': subject,
            'text': message
        }

        response = requests.post(url, auth=('api', api_key), data=data)
        response.raise_for_status()  # Raise an exception if the request was not successful
