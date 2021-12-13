from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.timezone import now


# class IpMoodel(models.Model):
#     ip = models.CharField(max_length=100)

#     def __str__(self):
#         return self.ip


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    author=models.CharField(max_length=20)
    author_pic = models.ImageField(null=True, blank=True)
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    slider = models.BooleanField(null=True, blank=True)
    # views = models.ManyToManyField(IpMoodel, related_name="post_views", blank=True)

    def __str__(self):
        return self.title + " by " + self.author


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username




# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)
#     content = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.content[0:13] + "..." + "by" + " " + self.user.username