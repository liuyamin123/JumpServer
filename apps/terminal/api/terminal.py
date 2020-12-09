# -*- coding: utf-8 -*-
#
from collections import OrderedDict
import logging
import uuid

from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny

from common.drf.api import JMSBulkModelViewSet
from common.utils import get_object_or_none
from common.permissions import IsAppUser, IsOrgAdminOrAppUser, IsSuperUser
from ..models import Terminal, Session
from .. import serializers
from .. import exceptions
from ..utils import TerminalStateUtil

__all__ = [
    'TerminalViewSet', 'TerminalTokenApi', 'StateViewSet', 'TerminalConfig',
]
logger = logging.getLogger(__file__)


class TerminalViewSet(JMSBulkModelViewSet):
    queryset = Terminal.objects.filter(is_deleted=False)
    serializer_class = serializers.TerminalSerializer
    permission_classes = (IsSuperUser,)
    filter_fields = ['name', 'remote_addr']

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            raise exceptions.BulkCreateNotSupport()

        name = request.data.get('name')
        remote_ip = request.META.get('REMOTE_ADDR')
        x_real_ip = request.META.get('X-Real-IP')
        remote_addr = x_real_ip or remote_ip

        terminal = get_object_or_none(Terminal, name=name, is_deleted=False)
        if terminal:
            msg = 'Terminal name %s already used' % name
            return Response({'msg': msg}, status=409)

        serializer = self.serializer_class(data={
            'name': name, 'remote_addr': remote_addr
        })

        if serializer.is_valid():
            terminal = serializer.save()

            # App should use id, token get access key, if accepted
            token = uuid.uuid4().hex
            cache.set(token, str(terminal.id), 3600)
            data = {"id": str(terminal.id), "token": token, "msg": "Need accept"}
            return Response(data, status=201)
        else:
            data = serializer.errors
            logger.error("Register terminal error: {}".format(data))
            return Response(data, status=400)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()


class TerminalTokenApi(APIView):
    permission_classes = (AllowAny,)
    queryset = Terminal.objects.filter(is_deleted=False)

    def get(self, request, *args, **kwargs):
        try:
            terminal = self.queryset.get(id=kwargs.get('terminal'))
        except Terminal.DoesNotExist:
            terminal = None

        token = request.query_params.get("token")

        if terminal is None:
            return Response('May be reject by administrator', status=401)

        if token is None or cache.get(token, "") != str(terminal.id):
            return Response('Token is not valid', status=401)

        if not terminal.is_accepted:
            return Response("Terminal was not accepted yet", status=400)

        if not terminal.user or not terminal.user.access_key:
            return Response("No access key generate", status=401)

        access_key = terminal.user.access_key()
        data = OrderedDict()
        data['access_key'] = {'id': access_key.id, 'secret': access_key.secret}
        return Response(data, status=200)


class StateViewSet(viewsets.GenericViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = serializers.StateSerializer
    task_serializer_class = serializers.TaskSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAppUser,)
        return super().get_permissions()

    @property
    def terminal(self):
        return self.request.user.terminal

    @staticmethod
    def initial_util(terminals_id):
        return TerminalStateUtil(terminals_id)

    def handle_data(self, data):
        util = self.initial_util(self.terminal.id)
        util.handle_data(data)

    def get_response(self):
        tasks = self.terminal.task_set.filter(is_finished=False)
        serializer = self.task_serializer_class(tasks, many=True)
        return Response(serializer.data, status=201)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.handle_data(serializer.data)
        response = self.get_response()
        return response

    def list(self, request, *args, **kwargs):
        terminal_type = request.query_params.get('terminal_type')
        if not terminal_type:
            return Response([], status=200)
        terminals_id = Terminal.objects.filter(type=terminal_type).values_list('id', flat=True)
        if not terminals_id:
            return Response([], status=200)
        util = self.initial_util(list(terminals_id))
        data = util.get_many_data()
        return Response(data, status=200)


class TerminalConfig(APIView):
    permission_classes = (IsAppUser,)

    def get(self, request):
        user = request.user
        terminal = user.terminal
        configs = terminal.config
        return Response(configs, status=200)