# -*- coding: utf-8 -*-
#

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from ..models import MyAsset

__all__ = ['MyAssetSerializer']


class CustomAttrsSerializer(serializers.Serializer):
    name = serializers.CharField(label=_("Custom Name"), max_length=128, allow_blank=True, required=False)
    comment = serializers.CharField(label=_("Custom Comment"), max_length=512, allow_blank=True, required=False)


class MyAssetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    custom_attrs = CustomAttrsSerializer()

    class Meta:
        model = MyAsset
        fields = ['user', 'asset', 'custom_attrs']
