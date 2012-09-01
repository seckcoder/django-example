# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'aggregation_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'aggregation', ['Author'])

        # Adding M2M table for field friends on 'Author'
        db.create_table(u'aggregation_author_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_author', models.ForeignKey(orm[u'aggregation.author'], null=False)),
            ('to_author', models.ForeignKey(orm[u'aggregation.author'], null=False))
        ))
        db.create_unique(u'aggregation_author_friends', ['from_author_id', 'to_author_id'])

        # Adding model 'Publisher'
        db.create_table(u'aggregation_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('num_awards', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'aggregation', ['Publisher'])

        # Adding model 'Book'
        db.create_table(u'aggregation_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('pages', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aggregation.Publisher'])),
            ('pubdate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'aggregation', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table(u'aggregation_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'aggregation.book'], null=False)),
            ('author', models.ForeignKey(orm[u'aggregation.author'], null=False))
        ))
        db.create_unique(u'aggregation_book_authors', ['book_id', 'author_id'])

        # Adding model 'Store'
        db.create_table(u'aggregation_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'aggregation', ['Store'])

        # Adding M2M table for field books on 'Store'
        db.create_table(u'aggregation_store_books', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('store', models.ForeignKey(orm[u'aggregation.store'], null=False)),
            ('book', models.ForeignKey(orm[u'aggregation.book'], null=False))
        ))
        db.create_unique(u'aggregation_store_books', ['store_id', 'book_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'aggregation_author')

        # Removing M2M table for field friends on 'Author'
        db.delete_table('aggregation_author_friends')

        # Deleting model 'Publisher'
        db.delete_table(u'aggregation_publisher')

        # Deleting model 'Book'
        db.delete_table(u'aggregation_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('aggregation_book_authors')

        # Deleting model 'Store'
        db.delete_table(u'aggregation_store')

        # Removing M2M table for field books on 'Store'
        db.delete_table('aggregation_store_books')


    models = {
        u'aggregation.author': {
            'Meta': {'object_name': 'Author'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'blank': 'True', 'to': u"orm['aggregation.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'aggregation.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['aggregation.Author']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pages': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'pubdate': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['aggregation.Publisher']"}),
            'rating': ('django.db.models.fields.FloatField', [], {})
        },
        u'aggregation.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'num_awards': ('django.db.models.fields.IntegerField', [], {})
        },
        u'aggregation.store': {
            'Meta': {'object_name': 'Store'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['aggregation.Book']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['aggregation']