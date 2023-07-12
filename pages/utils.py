import requests
from django.conf import settings

def send_email_via_mailgun(subject, message, sender_email, recipient_list):
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
    return response
