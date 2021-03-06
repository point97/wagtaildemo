# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SectionedPage'
        db.create_table(u'demo_sectionedpage', (
            (u'multilingualpage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['demo.MultiLingualPage'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'demo', ['SectionedPage'])

        # Deleting field 'EnglishHomePage.body'
        db.delete_column(u'demo_englishhomepage', 'body')

        # Deleting field 'EnglishHomePage.multilingualpage_ptr'
        db.delete_column(u'demo_englishhomepage', u'multilingualpage_ptr_id')

        # Adding field 'EnglishHomePage.sectionedpage_ptr'
        db.add_column(u'demo_englishhomepage', u'sectionedpage_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['demo.SectionedPage'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'SpanishHomePage.body'
        db.delete_column(u'demo_spanishhomepage', 'body')

        # Deleting field 'SpanishHomePage.multilingualpage_ptr'
        db.delete_column(u'demo_spanishhomepage', u'multilingualpage_ptr_id')

        # Adding field 'SpanishHomePage.sectionedpage_ptr'
        db.add_column(u'demo_spanishhomepage', u'sectionedpage_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['demo.SectionedPage'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SectionedPage'
        db.delete_table(u'demo_sectionedpage')

        # Adding field 'EnglishHomePage.body'
        db.add_column(u'demo_englishhomepage', 'body',
                      self.gf('wagtail.wagtailcore.fields.RichTextField')(default='', blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'EnglishHomePage.multilingualpage_ptr'
        raise RuntimeError("Cannot reverse this migration. 'EnglishHomePage.multilingualpage_ptr' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'EnglishHomePage.multilingualpage_ptr'
        db.add_column(u'demo_englishhomepage', u'multilingualpage_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['demo.MultiLingualPage'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'EnglishHomePage.sectionedpage_ptr'
        db.delete_column(u'demo_englishhomepage', u'sectionedpage_ptr_id')

        # Adding field 'SpanishHomePage.body'
        db.add_column(u'demo_spanishhomepage', 'body',
                      self.gf('wagtail.wagtailcore.fields.RichTextField')(default='', blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SpanishHomePage.multilingualpage_ptr'
        raise RuntimeError("Cannot reverse this migration. 'SpanishHomePage.multilingualpage_ptr' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SpanishHomePage.multilingualpage_ptr'
        db.add_column(u'demo_spanishhomepage', u'multilingualpage_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['demo.MultiLingualPage'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'SpanishHomePage.sectionedpage_ptr'
        db.delete_column(u'demo_spanishhomepage', u'sectionedpage_ptr_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'demo.englishhomepage': {
            'Meta': {'object_name': 'EnglishHomePage', '_ormbases': [u'demo.SectionedPage']},
            u'sectionedpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['demo.SectionedPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.langrootpage': {
            'Meta': {'object_name': 'LangRootPage', '_ormbases': [u'wagtailcore.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.multilingualpage': {
            'Meta': {'object_name': 'MultiLingualPage', '_ormbases': [u'wagtailcore.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'spanish_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"})
        },
        u'demo.sectionedpage': {
            'Meta': {'object_name': 'SectionedPage', '_ormbases': [u'demo.MultiLingualPage']},
            u'multilingualpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['demo.MultiLingualPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.sectionpage': {
            'Meta': {'object_name': 'SectionPage', '_ormbases': [u'wagtailcore.Page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'demo.spanishhomepage': {
            'Meta': {'object_name': 'SpanishHomePage', '_ormbases': [u'demo.SectionedPage']},
            u'sectionedpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['demo.SectionedPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'wagtailcore.page': {
            'Meta': {'object_name': 'Page'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'has_unpublished_changes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_pages'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'search_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['demo']