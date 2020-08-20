from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    article_image = models.ImageField(upload_to = 'articles/')
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100,default='Kenya') 
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
    @classmethod
    def get_author_post(cls,author):
        return cls.objects.filter(author=author)
        
class PostImage(models.Model):
    
    post = models.ForeignKey(Post,default=None,related_name='postimage',on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')
   
    def __str__(self):
        return self.post.title
    
   