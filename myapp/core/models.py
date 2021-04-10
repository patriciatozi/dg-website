from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):

    """
    Model representing every post published by Data Girls members
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tag = models.ManyToManyField('Tag')

    image = models.ImageField(default='src/img/default.png')

    class Meta:
        ordering = ['-created_on']
        db_table = 'table_posts'

    def __str__(self):
        return self.title


class Tag(models.Model):

    """
    Model representing the tag for each post
    """

    word = models.CharField(max_length=35)
    slug = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.word


class SocialMedia(models.Model):

    """
    Model created for each social media instance
    """

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(default='static/img/default.png')
