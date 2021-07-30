from django.db import models
from django.db.models.fields.related import OneToOneField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 

class Category (models.Model):

    Max_Length_title =128
    

    name = models.CharField(max_length=Max_Length_title, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique= True)
    def save (self, *args,**kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)
    class meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    Max_Length_title =128
    Max_Length_url= 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField (max_length=Max_Length_title)
    url = models.URLField(max_length=Max_Length_url)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile (models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to ='profile_images',blank=True)

    def __str__(self):
        return self.user.username