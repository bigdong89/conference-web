import requests

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def _get_from_settings(key):
    value = getattr(settings, key, None)

    if not value:
        raise ImproperlyConfigured("{} setting not set.".format(key))

    return value


def get_notifications_webhook():
    return _get_from_settings('SLACK_NOTIFICATIONS_WEBHOOK')


def post_notification(title, text, footer=None, fallback=None):
    url = get_notifications_webhook()

    default_fallback = "\n".join([title, text])

    attachment = {
        "title": title,
        "text": text,
        "fallback": fallback or default_fallback,
        "mrkdwn_in": ["text", "footer"],
        "color": "#9013FD"
    }

    if footer:
        attachment.update({
            "footer": footer,
            "footer_icon": "https://2018.webcampzg.org/static/images/heart-16px.png",
        })

    response = requests.post(url, json={
        "attachments": [attachment],
    })

    response.raise_for_status()
