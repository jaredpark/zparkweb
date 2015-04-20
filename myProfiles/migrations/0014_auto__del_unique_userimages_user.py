# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'UserImages', fields ['user']
        db.delete_unique('myProfiles_userimages', ['user_id'])


    def backwards(self, orm):
        # Adding unique constraint on 'UserImages', fields ['user']
        db.create_unique('myProfiles_userimages', ['user_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myProfiles.userimages': {
            'Meta': {'object_name': 'UserImages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myProfiles.UserProfile']", 'related_name': "'images'"}),
            'user_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'})
        },
        'myProfiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'balance_due_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'default': "''"}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'default': "''"}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'blank': 'True', 'default': '0.0', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '60', 'blank': 'True', 'default': "''"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True', 'default': "''"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True', 'default': "''"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'blank': 'True', 'default': '0.0', 'decimal_places': '2'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True', 'default': "'http://www.none.com'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'blank': 'True', 'default': '1'})
        },
        'myProfiles.userproject': {
            'Meta': {'object_name': 'UserProject'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'default': "'Project'"}),
            'design_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'progress_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'default': "'http://www.none.com'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myProfiles.UserProfile']", 'related_name': "'project'"})
        },
        'myProfiles.usersupport': {
            'Meta': {'object_name': 'UserSupport'},
            'has_basic_support': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_monthly_support': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_hours': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'blank': 'True', 'default': '0', 'decimal_places': '2', 'null': 'True'}),
            'monthly_hours_remaining': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'blank': 'True', 'default': '0', 'decimal_places': '2', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['myProfiles.UserProfile']", 'related_name': "'support'"})
        }
    }

    complete_apps = ['myProfiles']