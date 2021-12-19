from abc import ABC

from django.contrib.auth.models import User, Group
from quickstart.models import Documents, RateDocuments
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class DocumentsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ['url', 'title', ]

class DocumentsSerializer(serializers.Serializer, ABC):
    document = serializers.HyperlinkedModelSerializer(Documents)
    rate_avg = serializers.IntegerField(read_only=True)
    user_count = serializers.IntegerField(read_only=True)


class RateDocumentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RateDocuments
        fields = ['url', 'document', 'user', 'rate', ]


class MDocumentsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    text = serializers.CharField(style={'base_template': 'textarea.html'})
    rate = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Documents` instance, given the validated data.
        """
        return Documents.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Documents` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.save()
        return instance
