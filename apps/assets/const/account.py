from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class Connectivity(TextChoices):
    UNKNOWN = 'unknown', _('Unknown')
    OK = 'ok', _('Ok')
    FAILED = 'failed', _('Failed')


class SecretType(TextChoices):
    PASSWORD = 'password', _('Password')
    SSH_KEY = 'ssh_key', _('SSH key')
    ACCESS_KEY = 'access_key', _('Access key')
    TOKEN = 'token', _('Token')


class AliasAccount(TextChoices):
    ALL = '@ALL', _('All')
    INPUT = '@INPUT', _('Manual input')
    USER = '@USER', _('Dynamic user')


class Source(TextChoices):
    LOCAL = 'local', _('Local')
    COLLECTED = 'collected', _('Collected')
