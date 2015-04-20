# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserImages.logo'
        db.add_column('myProfiles_userimages', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserImages.logo'
        db.delete_column('myProfiles_userimages', 'logo')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myProfiles.userfiles': {
            'Meta': {'object_name': 'UserFiles'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myProfiles.UserProfile']", 'related_name': "'files'"}),
            'user_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'myProfiles.userimages': {
            'Meta': {'object_name': 'UserImages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myProfiles.UserProfile']", 'related_name': "'images'"}),
            'user_image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'})
        },
        'myProfiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '100'}),
            'balance_due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '20'}),
            'company': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '100'}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'decimal_places': '2', 'blank': 'True', 'max_digits': '6'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'blank': 'True', 'max_length': '60'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True', 'max_length': '400'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '12'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_balance': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'decimal_places': '2', 'blank': 'True', 'max_digits': '6'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "'http://www.none.com'", 'blank': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True', 'max_length': '5'})
        },
        'myProfiles.userproject': {
            'Meta': {'object_name': 'UserProject'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'Project'", 'max_length': '400'}),
            'design_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress_url': ('django.db.models.fields.URLField', [], {'default': "'http://www.none.com'", 'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myProfiles.UserProfile']", 'related_name': "'project'"})
        },
        'myProfiles.usersupport': {
            'Meta': {'object_name': 'UserSupport'},
            'has_basic_support': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_monthly_support': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_hours': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'decimal_places': '2', 'blank': 'True', 'max_digits': '3'}),
            'monthly_hours_remaining': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'decimal_places': '2', 'blank': 'True', 'max_digits': '3'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myProfiles.UserProfile']", 'related_name': "'support'"})
        }
    }

    complete_apps = ['myProfiles']