from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *



class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogHome(models.Model):
    title =models.CharField(max_length=1000)
    content=FroalaField()
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='picture')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogHome, self).save(*args, **kwargs)
   

    
    

     


