# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table('blog_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tagline', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('blog', ['Blog'])

        # Adding model 'Author'
        db.create_table('blog_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('blog', ['Author'])

        # Adding model 'Entry'
        db.create_table('blog_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Blog'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body_text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('mod_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('n_comments', self.gf('django.db.models.fields.IntegerField')()),
            ('n_pingbacks', self.gf('django.db.models.fields.IntegerField')()),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('blog', ['Entry'])

        # Adding M2M table for field authors on 'Entry'
        db.create_table('blog_entry_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['blog.entry'], null=False)),
            ('author', models.ForeignKey(orm['blog.author'], null=False))
        ))
        db.create_unique('blog_entry_authors', ['entry_id', 'author_id'])

        # Adding model 'User'
        db.create_table('blog_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('blog', ['User'])

        # Adding model 'Message'
        db.create_table('blog_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.User'])),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Message'], null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Message'])

        # Adding model 'Forum'
        db.create_table('blog_forum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=24)),
        ))
        db.send_create_signal('blog', ['Forum'])

        # Adding model 'Message_forum'
        db.create_table('blog_message_forum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Message'])),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Forum'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Message_forum'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('blog_blog')

        # Deleting model 'Author'
        db.delete_table('blog_author')

        # Deleting model 'Entry'
        db.delete_table('blog_entry')

        # Removing M2M table for field authors on 'Entry'
        db.delete_table('blog_entry_authors')

        # Deleting model 'User'
        db.delete_table('blog_user')

        # Deleting model 'Message'
        db.delete_table('blog_message')

        # Deleting model 'Forum'
        db.delete_table('blog_forum')

        # Deleting model 'Message_forum'
        db.delete_table('blog_message_forum')


    models = {
        'blog.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tagline': ('django.db.models.fields.TextField', [], {})
        },
        'blog.entry': {
            'Meta': {'object_name': 'Entry'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Author']", 'symmetrical': 'False'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Blog']"}),
            'body_text': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mod_date': ('django.db.models.fields.DateTimeField', [], {}),
            'n_comments': ('django.db.models.fields.IntegerField', [], {}),
            'n_pingbacks': ('django.db.models.fields.IntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        },
        'blog.forum': {
            'Meta': {'object_name': 'Forum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.Message']", 'null': 'True', 'through': "orm['blog.Message_forum']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'blog.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Message']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.User']"})
        },
        'blog.message_forum': {
            'Meta': {'object_name': 'Message_forum'},
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Forum']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Message']"}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'blog.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']