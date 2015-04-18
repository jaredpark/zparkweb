# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.raw_data'
        db.delete_column('myProfiles_userprofile', 'raw_data')

        # Deleting field 'UserProfile.has_dog'
        db.delete_column('myProfiles_userprofile', 'has_dog')

        # Deleting field 'UserProfile.date_of_birth'
        db.delete_column('myProfiles_userprofile', 'date_of_birth')

        # Deleting field 'UserProfile.facebook_name'
        db.delete_column('myProfiles_userprofile', 'facebook_name')

        # Deleting field 'UserProfile.facebook_open_graph'
        db.delete_column('myProfiles_userprofile', 'facebook_open_graph')

        # Deleting field 'UserProfile.next_appointment'
        db.delete_column('myProfiles_userprofile', 'next_appointment')

        # Deleting field 'UserProfile.website_url'
        db.delete_column('myProfiles_userprofile', 'website_url')

        # Deleting field 'UserProfile.facebook_profile_url'
        db.delete_column('myProfiles_userprofile', 'facebook_profile_url')

        # Deleting field 'UserProfile.locked_gate'
        db.delete_column('myProfiles_userprofile', 'locked_gate')

        # Deleting field 'UserProfile.public'
        db.delete_column('myProfiles_userprofile', 'public')

        # Deleting field 'UserProfile.pest_customer'
        db.delete_column('myProfiles_userprofile', 'pest_customer')

        # Deleting field 'UserProfile.image'
        db.delete_column('myProfiles_userprofile', 'image')

        # Deleting field 'UserProfile.new_token_required'
        db.delete_column('myProfiles_userprofile', 'new_token_required')

        # Deleting field 'UserProfile.blog_url'
        db.delete_column('myProfiles_userprofile', 'blog_url')

        # Deleting field 'UserProfile.facebook_id'
        db.delete_column('myProfiles_userprofile', 'facebook_id')

        # Deleting field 'UserProfile.access_token'
        db.delete_column('myProfiles_userprofile', 'access_token')

        # Deleting field 'UserProfile.weed_customer'
        db.delete_column('myProfiles_userprofile', 'weed_customer')

        # Deleting field 'UserProfile.gender'
        db.delete_column('myProfiles_userprofile', 'gender')

        # Deleting field 'UserProfile.about_me'
        db.delete_column('myProfiles_userprofile', 'about_me')

        # Adding field 'UserProfile.company'
        db.add_column('myProfiles_userprofile', 'company',
                      self.gf('django.db.models.fields.CharField')(max_length=100, default='', blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.url'
        db.add_column('myProfiles_userprofile', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=100, default='http://www.none.com', blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.total_balance'
        db.add_column('myProfiles_userprofile', 'total_balance',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2, default=0.0, blank=True),
                      keep_default=False)


        # Changing field 'UserProfile.email'
        db.alter_column('myProfiles_userprofile', 'email', self.gf('django.db.models.fields.EmailField')(max_length=60))

        # Changing field 'UserProfile.address'
        db.alter_column('myProfiles_userprofile', 'address', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Adding field 'UserProfile.raw_data'
        db.add_column('myProfiles_userprofile', 'raw_data',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.has_dog'
        db.add_column('myProfiles_userprofile', 'has_dog',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.date_of_birth'
        db.add_column('myProfiles_userprofile', 'date_of_birth',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_name'
        db.add_column('myProfiles_userprofile', 'facebook_name',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_open_graph'
        db.add_column('myProfiles_userprofile', 'facebook_open_graph',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.next_appointment'
        db.add_column('myProfiles_userprofile', 'next_appointment',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.website_url'
        db.add_column('myProfiles_userprofile', 'website_url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_profile_url'
        db.add_column('myProfiles_userprofile', 'facebook_profile_url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.locked_gate'
        db.add_column('myProfiles_userprofile', 'locked_gate',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.public'
        db.add_column('myProfiles_userprofile', 'public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.pest_customer'
        db.add_column('myProfiles_userprofile', 'pest_customer',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.image'
        db.add_column('myProfiles_userprofile', 'image',
                      self.gf('utilities.ContentTypeRestrictedImageField')(max_length=255, null=True, blank=True, max_upload_size=2621440),
                      keep_default=False)

        # Adding field 'UserProfile.new_token_required'
        db.add_column('myProfiles_userprofile', 'new_token_required',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.blog_url'
        db.add_column('myProfiles_userprofile', 'blog_url',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_id'
        db.add_column('myProfiles_userprofile', 'facebook_id',
                      self.gf('django.db.models.fields.BigIntegerField')(unique=True, blank=True, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.access_token'
        db.add_column('myProfiles_userprofile', 'access_token',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.weed_customer'
        db.add_column('myProfiles_userprofile', 'weed_customer',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserProfile.gender'
        db.add_column('myProfiles_userprofile', 'gender',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.about_me'
        db.add_column('myProfiles_userprofile', 'about_me',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'UserProfile.company'
        db.delete_column('myProfiles_userprofile', 'company')

        # Deleting field 'UserProfile.url'
        db.delete_column('myProfiles_userprofile', 'url')

        # Deleting field 'UserProfile.total_balance'
        db.delete_column('myProfiles_userprofile', 'total_balance')


        # Changing field 'UserProfile.email'
        db.alter_column('myProfiles_userprofile', 'email', self.gf('django.db.models.fields.EmailField')(max_length=40))

        # Changing field 'UserProfile.address'
        db.alter_column('myProfiles_userprofile', 'address', self.gf('django.db.models.fields.CharField')(max_length=60))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myProfiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'balance_due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''", 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100', 'default': "''", 'blank': 'True'}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2', 'default': '0.0', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '60', 'default': "''", 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'default': "''", 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'default': "''", 'blank': 'True'}),
            'total_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2', 'default': '0.0', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '100', 'default': "'http://www.none.com'", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'default': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['myProfiles']