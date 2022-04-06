from asyncore import read
from rest_framework import serializers
from apps.blogs.models import Blog,Vote,Comment

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    votes = serializers.SerializerMethodField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    slug = serializers.SlugField(read_only = True)

    class Meta:
        model = Blog
        fields = ['title','slug','content','author','created_at','updated_at','votes','comments']

    def get_votes(self, blog):
        return Vote.objects.filter(blog=blog).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['user','content','blog','parent_comment']