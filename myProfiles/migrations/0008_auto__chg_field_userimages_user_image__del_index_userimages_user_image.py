# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'UserImages.user_image' to match new field type.
        db.rename_column('myProfiles_userimages', 'user_image_id', 'user_image')
        # Changing field 'UserImages.user_image'
        db.alter_column('myProfiles_userimages', 'user_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))
        # Removing index on 'UserImages', fields ['user_image']
        db.delete_index('myProfiles_userimages', ['user_image_id'])


    def backwards(self, orm):
        # Adding index on 'UserImages', fields ['user_image']
        db.create_index('myProfiles_userimages', ['user_image_id'])


        # Renaming column for 'UserImages.user_image' to match new field type.
        db.rename_column('myProfiles_userimages', 'user_image', 'user_image_id')
        # Changing field 'UserImages.user_image'
        db.alter_column('myProfiles_userimages', 'user_image_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['filer.Image']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myProfiles.userimages': {
            'Meta': {'object_name': 'UserImages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'unique': 'True', 'to': "orm['myProfiles.UserProfile']"}),
            'user_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'})
        },
        'myProfiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '100'}),
            'balance_due_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '20'}),
            'company': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '100'}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'blank': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'blank': 'True', 'max_length': '60'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True', 'max_length': '400'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '12'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_balance': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'blank': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "'http://www.none.com'", 'blank': 'True', 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True', 'max_length': '5'})
        }
    }

    complete_apps = ['myProfiles']