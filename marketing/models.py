from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email


class Signup(models.Model):
    email = models.EmailField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email


class MainContent(models.Model):
    maintitle = models.CharField(max_length=100)
    maincontent = RichTextField()
    featured = models.BooleanField(null=True, blank=True)
    # overview = models.TextField()
    # slug = models.SlugField(max_length=100, blank=True, null=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    # author=models.CharField(max_length=20)
    # author_pic = models.ImageField(null=True, blank=True)
    # thumbnail = models.ImageField()
    # slider = models.BooleanField(null=True, blank=True)
    # views = models.ManyToManyField(IpMoodel, related_name="post_views", blank=True)

    def __str__(self):
        return self.maintitle



class About(models.Model):
    maintitle = models.CharField(max_length=100)
    maincontent = RichTextField()
    featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.maintitle
    
class Resume(models.Model):
    resumetitle = models.CharField(max_length=100)
    resumecontent = RichTextField()
    featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.resumetitle

class AboutSocial(models.Model):
    socilaTitle = models.CharField(max_length=100, null=True, blank=True)
    socilaLink = models.CharField(max_length=100, null=True, blank=True)
    socilColor = models.CharField(max_length=100, null=True, blank=True)
    featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.socilaTitle
    

class FooterSocial(models.Model):
    socilaTitle = models.CharField(max_length=100, null=True, blank=True)
    socilaLink = models.CharField(max_length=100, null=True, blank=True)
    socilColor = models.CharField(max_length=100, null=True, blank=True)
    featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.socilaTitle


class Aboutbulletin(models.Model):
    bulletinTitle = models.TextField(null=True, blank=True)
    bulletinLink = models.CharField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.bulletinTitle[0:60]