from rest_framework import serializers


from simpleblog.models import Entry, Category


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.get_absolute_url()

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'slug', 'seo_title', 'seo_description', 'url'
        )


class EntrySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.get_absolute_url()

    class Meta:
        model = Entry
        fields = (
            'id', 'title', 'slug', 'image', 'intro',
            'publication_date', 'seo_title', 'seo_description',
            'modified', 'author', 'category', 'url', 'published',
        )


class EntryDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.get_absolute_url()

    class Meta:
        model = Entry
        fields = (
            'id', 'title', 'slug', 'image', 'intro', 'content',
            'publication_date', 'seo_title', 'seo_description',
            'modified', 'author', 'category', 'url'
        )