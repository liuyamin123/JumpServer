# -*- coding: utf-8 -*-
#
from common.api import JMSModelViewSet
from common.permissions import IsValidUser
from rest_framework.response import Response
from ..models import MyAsset, Asset
from ..serializers import MyAssetSerializer

__all__ = ['MyAssetViewSet']


class MyAssetViewSet(JMSModelViewSet):
    serializer_class = MyAssetSerializer
    permission_classes = (IsValidUser,)
    filterset_fields = ['asset']

    def get_queryset(self):
        queryset = MyAsset.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        custom_attrs = data.get('custom_attrs', {})
        defaults = {'custom_attrs': custom_attrs}
        obj, created = MyAsset.objects.get_or_create(
            defaults=defaults,
            user=request.user,
            asset=data.get('asset')
        )
        if not created:
            obj.custom_attrs.update(custom_attrs)
            obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
