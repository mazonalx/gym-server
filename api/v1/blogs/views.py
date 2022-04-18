from urllib import request
from rest_framework import generics,permissions,mixins,status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.blogs.models import Blog,Vote,Comment
from .serializers import BlogSerializer,VoteSerializer,CommentSerializer
from .permissions import IsOwnerOrReadOnly

class BlogList(generics.ListCreateAPIView): 
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializers):
        serializers.save(author = self.request.user)
        
class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    lookup_field ='slug'

    def delete(self,request, *args, **kwargs):
        blog = Blog.objects.filter(slug=kwargs['slug'],author=self.request.user)
        if blog.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This isn\'t your blog to delete BRUH!')
            
    def put(self, request, *args,**kwargs):
        blog = Blog.objects.filter(slug=kwargs['slug'],author=self.request.user)
        if blog.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('This isn\'t your blog to update BRUH!')

class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin): 
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated,]
    
    def get_queryset(self):
        user = self.request.user
        blog = Blog.objects.get(slug=self.kwargs['slug'])
        return Vote.objects.filter(voter=user, blog=blog)

    def perform_create(self, serializers):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this blog :)')
        serializers.save(voter = self.request.user, blog = Blog.objects.get(slug=self.kwargs['slug']))
    
    def delete(self,request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted for this blog...silly!')

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]