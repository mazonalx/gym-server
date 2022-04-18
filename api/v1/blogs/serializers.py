from cgitb import lookup
from rest_framework import serializers
from apps.blogs.models import Blog,Vote,Comment

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    blog = serializers.ReadOnlyField(source='blog.slug')
    class Meta:
        model = Comment
        fields = ['id','user','content','blog','parent_comment']

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    slug = serializers.SlugField(read_only = True)
    votes = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['title','slug','content','author','votes','created_at','updated_at']

    def get_votes(self, blog):
        return Vote.objects.filter(blog=blog).count()