from rest_framework import serializers
from ..models import Comment
from common.fields.serializer import CanReadHiddenField

__all__ = ['CommentSerializer']


class CurrentTicket(object):
    ticket = None

    def set_context(self, serializer_field):
        self.ticket = serializer_field.context['ticket']

    def __call__(self):
        return self.ticket


class CommentSerializer(serializers.ModelSerializer):
    ticket = CanReadHiddenField(default=CurrentTicket())
    user = CanReadHiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            'id', 'ticket', 'body', 'user', 'user_display', 'date_created', 'date_updated'
        ]
        read_only_fields = [
            'user_display', 'date_created', 'date_updated'
        ]
