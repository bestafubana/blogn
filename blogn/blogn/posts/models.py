from django.db import models
from django.contrib.auth.models import User

class PostManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(body__icontains=query))

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    pub_date = models.DateTimeField('Publication Date', auto_now_add=True)
    mod_date = models.DateTimeField('Modification Date', auto_now=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    excerpt = models.CharField(max_length=250, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User)
    
    DRAFT = 'DR'
    PUBLISHED = 'PB'
    STATUS_CHOICES = (
        (DRAFT, 'draft'),
        (PUBLISHED, 'published'),
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    def __str__(self):
        return self.getLongDate() + " - " + self.title

    def getLongDate(self):
        return self.pub_date.strftime('%b %e %Y @ %H:%M')

    def getShortDate(self):
        return self.pub_date.strftime('%b, %e %Y')     
    
    def summary(self):
        return self.body[:100]
        
    @models.permalink    
    def get_absolute_url(self):
        return ('postsingle', (), {'slug': self.slug} )
        
    objects = PostManager()    
    
    class Meta:
        # verbose_name=''
        # verbose_name_plural=''
        ordering = ['-pub_date']

class Comment(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    parent_comment = models.ForeignKey("self", null=True, blank=True)
    body = models.TextField(max_length=1024)
    pub_date = models.DateTimeField('Publication Date', auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.pub_date.strftime('%b, %e %Y') + " - " + self.author.username + " - " + self.body[:30] + "..."
    
    # class Meta:
        # verbose_name=''
        # verbose_name_plural=''
        # ordering = ['pub_date']