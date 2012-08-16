from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    def __unicode__(self):
        return self.name

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

class User(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
class Message(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey('User')
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
