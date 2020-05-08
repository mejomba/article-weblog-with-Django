from rest_framework import serializers


class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=4096)
    created_at = serializers.DateTimeField(required=True)


class SubmitArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    author_id = serializers.IntegerField(required=True, allow_null=False)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=4096)
    abstract = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    category_id = serializers.IntegerField(required=True, allow_null=False)
    promote = serializers.BooleanField(required=True, allow_null=False)


# TODO cover update API to wrong directory
class CoverUpdate(serializers.Serializer):
    article_id = serializers.IntegerField(required=True, allow_null=False)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)


class DeleteArticleSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True, allow_null=False)