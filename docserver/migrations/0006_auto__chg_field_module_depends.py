# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Module.depends'
        db.alter_column(u'docserver_module', 'depends', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Module.depends'
        raise RuntimeError("Cannot reverse this migration. 'Module.depends' and its values cannot be restored.")

    models = {
        u'docserver.collection': {
            'Meta': {'object_name': 'Collection'},
            'collectionid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'root_directory': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'docserver.derivedfile': {
            'Meta': {'object_name': 'DerivedFile'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'derived_from': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docserver.SourceFile']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'derivedfiles'", 'to': u"orm['docserver.Document']"}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'module_version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docserver.ModuleVersion']"}),
            'outputname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'docserver.derivedfilepart': {
            'Meta': {'object_name': 'DerivedFilePart'},
            'derivedfile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parts'", 'to': u"orm['docserver.DerivedFile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part_order': ('django.db.models.fields.IntegerField', [], {}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        u'docserver.document': {
            'Meta': {'object_name': 'Document'},
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'to': u"orm['docserver.Collection']"}),
            'external_identifier': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'docserver.documentlogmessage': {
            'Meta': {'ordering': "['-datetime']", 'object_name': 'DocumentLogMessage'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'logs'", 'to': u"orm['docserver.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'moduleversion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docserver.ModuleVersion']", 'null': 'True', 'blank': 'True'}),
            'sourcefile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docserver.SourceFile']", 'null': 'True', 'blank': 'True'})
        },
        u'docserver.essentiaversion': {
            'Meta': {'object_name': 'EssentiaVersion'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sha1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'docserver.module': {
            'Meta': {'object_name': 'Module'},
            'collections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['docserver.Collection']", 'symmetrical': 'False'}),
            'depends': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'source_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docserver.SourceFileType']"})
        },
        u'docserver.moduleversion': {
            'Meta': {'object_name': 'ModuleVersion'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docserver.Module']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'docserver.sourcefile': {
            'Meta': {'object_name': 'SourceFile'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sourcefiles'", 'to': u"orm['docserver.Document']"}),
            'file_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['docserver.SourceFileType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'docserver.sourcefiletype': {
            'Meta': {'object_name': 'SourceFileType'},
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['docserver']