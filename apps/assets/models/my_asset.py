from django.db import models
from django.utils.translation import gettext_lazy as _

from common.db.models import JMSBaseModel

__all__ = ['MyAsset']


class MyAsset(JMSBaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    asset = models.ForeignKey('assets.Asset', on_delete=models.CASCADE)
    custom_attrs = models.JSONField(default=dict)

    class Meta:
        unique_together = ('user', 'asset')
        verbose_name = _("My asset")

    def __str__(self):
        return '%s' % self.asset
