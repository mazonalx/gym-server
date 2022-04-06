from statistics import mode
from django.db import models
from apps.accounts.models import TimestampedModel
from django.contrib.auth import get_user_model
from slugify import slugify

CustomUser = get_user_model()

class Blog(TimestampedModel):
    title = models.CharField(max_length=100)
    slug= models.SlugField(max_length=100,null=False, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_pics",blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_at']
    def __str__(self):
        return f'{self.author} | {self.title}'
    def get_absolute_url(self):
        return f'/blogs/{self.slug}'
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
class Comment(TimestampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null= True, blank= True)

    def __str__(self):
        return f'{self.user.username} | Comment: {self.content}'

class Vote(TimestampedModel):
    voter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.voter.username} | {self.blog.title}'