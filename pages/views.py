from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.generic import FormView
from .forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages


class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/contact/success/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        try:
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,
                ['mk.moukangwe@gmail.com'],
                fail_silently=False,
            )
            messages.success(self.request, 'Thank you for contacting me! I will get back to you soon.')
        except:
            messages.error(self.request, 'An error occurred. Please try again later.')

        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
