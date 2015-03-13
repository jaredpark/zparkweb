# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('myProfiles_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about_me', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True, blank=True, null=True)),
            ('access_token', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('facebook_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True, null=True)),
            ('facebook_profile_url', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('website_url', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('blog_url', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True, null=True)),
            ('raw_data', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('facebook_open_graph', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
            ('new_token_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('utilities.ContentTypeRestrictedImageField')(max_length=255, max_upload_size=2621440, blank=True, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(unique=True, to=orm['auth.User'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20, default='')),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20, default='')),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True, default='')),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True, default='')),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')(max_length=5, default=85111)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True, default='')),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=40, blank=True, default='')),
            ('has_dog', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('locked_gate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pest_customer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weed_customer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('current_balance', self.gf('django.db.models.fields.DecimalField')(max_digits=6, blank=True, decimal_places=2, default=0.0)),
            ('balance_due_date', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('next_appointment', self.gf('django.db.models.fields.DateField')(blank=True, null=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=400, blank=True, default='')),
        ))
        db.send_create_signal('myProfiles', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('myProfiles_userprofile')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myProfiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True', 'default': "''"}),
            'balance_due_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'blog_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'default': "''"}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'blank': 'True', 'decimal_places': '2', 'default': '0.0'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '40', 'blank': 'True', 'default': "''"}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'blank': 'True', 'null': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'facebook_open_graph': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True', 'null': 'True'}),
            'has_dog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('utilities.ContentTypeRestrictedImageField', [], {'max_length': '255', 'max_upload_size': '2621440', 'blank': 'True', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "''"}),
            'locked_gate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'new_token_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'next_appointment': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True', 'default': "''"}),
            'pest_customer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True', 'default': "''"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'unique': 'True', 'to': "orm['auth.User']"}),
            'website_url': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'weed_customer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'default': '85111'})
        }
    }

    complete_apps = ['myProfiles']