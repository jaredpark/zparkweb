# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table('myQuotes_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_text', self.gf('django.db.models.fields.TextField')()),
            ('quote_author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('quote_date', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('myQuotes', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table('myQuotes_quote')


    models = {
        'myQuotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'quote_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['myQuotes']