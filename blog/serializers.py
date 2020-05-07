from rest_framework import serializers


class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=1)
    cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=4)
    created_at = serializers.DateTimeField(required=True)
