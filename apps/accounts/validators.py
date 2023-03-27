from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import (
    UniqueTogetherValidator, ValidationError
)

from accounts.const import AccountExistPolicy
from accounts.models import Account
from assets.const import Protocol

__all__ = ['AccountUniqueTogetherValidator', 'AccountSecretTypeValidator']


class ValidatorStrategyMixin:

    @staticmethod
    def get_strategy(attrs):
        return attrs.get('strategy', AccountExistPolicy.SKIP)

    def __call__(self, attrs, serializer):
        return super().__call__(attrs, serializer)


class SecretTypeValidator:
    requires_context = True
    protocol_settings = Protocol.settings()
    message = _('{field_name} not a legal option')

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, attrs, serializer):
        secret_types = set()
        if serializer.instance:
            asset = serializer.instance.asset
        else:
            asset = attrs['asset']
        secret_type = attrs['secret_type']
        platform_protocols_dict = {
            name: self.protocol_settings.get(name, {}).get('secret_types', [])
            for name in asset.platform.protocols.values_list('name', flat=True)
        }

        for name in asset.protocols.values_list('name', flat=True):
            if name in platform_protocols_dict:
                secret_types |= set(platform_protocols_dict[name])
        if secret_type not in secret_types:
            message = self.message.format(field_name=secret_type)
            raise ValidationError(message, code='error')


class UpdateAccountMixin:
    fields: tuple
    get_strategy: callable

    def update(self, attrs):

        query = {field_name: attrs[field_name] for field_name in self.fields}
        account = Account.objects.filter(**query).first()

        for k, v in attrs.items():
            setattr(account, k, v)
        account.save()

    def __call__(self, attrs, serializer):
        try:
            super().__call__(attrs, serializer)
        except ValidationError as e:
            strategy = self.get_strategy(attrs)
            if strategy == AccountExistPolicy.UPDATE:
                self.update(attrs)
            message = e.detail[0]
            raise ValidationError(message, code='unique')


class AccountUniqueTogetherValidator(UniqueTogetherValidator):
    fields: tuple

    @staticmethod
    def get_on_exist_policy(attrs):
        return attrs.get('on_exist', AccountExistPolicy.ERROR)

    def __call__(self, attrs, serializer):
        message = None
        try:
            super().__call__(attrs, serializer)
        except ValidationError as e:
            message = e.detail[0]
        on_exist = self.get_on_exist_policy(attrs)
        if not message:
            return
        if on_exist == AccountExistPolicy.ERROR:
            raise ValidationError(message, code='error')
        elif on_exist in [AccountExistPolicy.SKIP, AccountExistPolicy.UPDATE]:
            raise ValidationError({})
        else:
            return


class AccountSecretTypeValidator(ValidatorStrategyMixin, SecretTypeValidator):
    pass
