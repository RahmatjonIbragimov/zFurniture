from email.policy import default
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='nom')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='link')

    #admin panel objectlari asl nomini ko'rsatadi
    def __str__(self):
        return self.title

    #alifbo tartibida obj.larni chiqaradi ['-ttt'] yo ['ttt']
    class Meta:
        ordering = ['title']

class Block(models.Model):
    view = models.ImageField(default=0, upload_to='photos/%y/%m/%d/', verbose_name='photo')
    title = models.CharField(max_length=100, verbose_name='nom', blank=True)
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey( Category, on_delete=models.PROTECT)
    
    #admin panel objectlari asl nomini ko'rsatadi
    def __str__(self):
        return self.title
 
    #alifbo tartibida obj.larni chiqaradi ['-ttt'] yo ['ttt']
    class Meta:
        ordering = ['title']


class Post(models.Model):
    pass

class archive(models.Model):
    pass

class contact(models.Model):
    pass


























