from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    update_date = models.DateTimeField(auto_now_add=True, auto_now=True,
                                       null=True, blank=True)

    def __unicode__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    update_date = models.DateField(auto_now_add=True, auto_now=True,
                                   blank=True, null=True)
    class Meta:
        unique_together = ("name", "update_date")
    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('author_detail', [str(self.id)])

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    def __unicode__(self):
        return self.headline

class MUser(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
class Message(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey('MUser')
    thread = models.ForeignKey('self', blank=True, null=True)
    def __unicode__(self):
        return '%s' % self.id
class Forum(models.Model):
    name = models.CharField(max_length=24)
    messages = models.ManyToManyField(Message, through='Message_forum',
                                      blank=True, null=True)
    def __unicode__(self):
        return self.name
class Message_forum(models.Model):
    message = models.ForeignKey(Message)
    forum = models.ForeignKey(Forum)
    status = models.IntegerField(default=0)
    position = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return '%s ---%s' % ( self.message, self.forum )
class FakeEntry(Entry):
    class Meta:
        proxy = True

class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=20)
    def title_detail(self):
        return mark_safe(u'<a href="/post/liwei">baidu</a>')
    title_detail.allow_tags = True
    class Meta:
        verbose_name = "Seckcoder Post"
        verbose_name_plural = "Seckcoder' Posts"

class StudyOrder(models.Model):
    author = models.ForeignKey(Author)
    update_date = models.DateField()
    class Meta:
        unique_together=("author", "update_date")
    def __unicode__(self):
        return '%s : %s' % (self.author, self.update_date)
