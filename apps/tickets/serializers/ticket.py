# -*- coding: utf-8 -*-
#
from rest_framework import serializers

from ..exceptions import (
    TicketClosed, OnlyTicketAssigneeCanOperate,
    TicketCanNotOperate
)
from ..models import Ticket, Comment

__all__ = ['TicketSerializer', 'CommentSerializer']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id', 'title', 'type', 'type_display', 'meta', 'body',
            'action', 'action_display', 'status',
            'applicant', 'applicant_display',
            'approver', 'approver_display',
            'assignees', 'assignees_display',
            'date_created', 'date_updated',
        ]
        read_only_fields = [
            'applicant_display', 'approver_display', 'assignees_display',
            'date_created', 'date_updated',
        ]

    def create(self, validated_data):
        validated_data.pop('action')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        action = validated_data.get('action')
        user = self.context['request'].user

        if instance.type not in (Ticket.TYPE.GENERAL,
                                 Ticket.TYPE.LOGIN_CONFIRM):
            # 暂时的兼容操作吧，后期重构工单
            raise TicketCanNotOperate

        if instance.status == instance.STATUS.CLOSED:
            raise TicketClosed

        if action:
            if user not in instance.assignees.all():
                raise OnlyTicketAssigneeCanOperate

            # 有 `action` 时忽略 `status`
            validated_data.pop('status', None)

            instance = super().update(instance, validated_data)
            if not instance.status == instance.STATUS.CLOSED and action:
                instance.perform_action(action, user)
        else:
            status = validated_data.get('status')
            instance = super().update(instance, validated_data)
            if status:
                instance.perform_status(status, user)

        return instance


class CurrentTicket(object):
    ticket = None

    def set_context(self, serializer_field):
        self.ticket = serializer_field.context['ticket']

    def __call__(self):
        return self.ticket


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    ticket = serializers.HiddenField(
        default=CurrentTicket()
    )

    class Meta:
        model = Comment
        fields = [
            'id', 'ticket', 'body', 'user', 'user_display',
            'date_created', 'date_updated'
        ]
        read_only_fields = [
            'user_display', 'date_created', 'date_updated'
        ]
