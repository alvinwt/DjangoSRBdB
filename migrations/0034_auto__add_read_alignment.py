# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Read_alignment'
        db.create_table(u'srb_read_alignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aligned_interval', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Interval'])),
            ('seq_run_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Sequencing_Run'])),
            ('genome_build_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Genome_Build'])),
            ('sequence', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('read_counts', self.gf('django.db.models.fields.IntegerField')(max_length=45)),
            ('mapped_strand', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('number_genomic_hits', self.gf('django.db.models.fields.FloatField')(max_length=45)),
        ))
        db.send_create_signal(u'srb', ['Read_alignment'])


    def backwards(self, orm):
        # Deleting model 'Read_alignment'
        db.delete_table(u'srb_read_alignment')


    models = {
        u'srb.genome_build': {
            'Meta': {'object_name': 'Genome_Build'},
            'genome_build_id': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'srb.interval': {
            'IntervalSerialNumber': ('django.db.models.fields.IntegerField', [], {'max_length': '45'}),
            'IntervalSize': ('django.db.models.fields.IntegerField', [], {'max_length': '45'}),
            'Link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Interval'},
            'NeatName': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'start': ('django.db.models.fields.IntegerField', [], {'max_length': '15'}),
            'stop': ('django.db.models.fields.IntegerField', [], {'max_length': '15'})
        },
        u'srb.library': {
            'Meta': {'ordering': "['library_id']", 'object_name': 'Library'},
            'allele': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'library_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'multiplex_barcode_sequence': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'organism': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'resolution': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'source_org': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'source_person': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'strain': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'tissue': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        u'srb.library_sequencing_run': {
            'Meta': {'object_name': 'Library_Sequencing_Run'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'library_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Library']"}),
            'seq_run_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Sequencing_Run']"})
        },
        u'srb.read_alignment': {
            'Meta': {'object_name': 'Read_alignment'},
            'aligned_interval': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Interval']"}),
            'genome_build_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Genome_Build']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapped_strand': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'number_genomic_hits': ('django.db.models.fields.FloatField', [], {'max_length': '45'}),
            'read_counts': ('django.db.models.fields.IntegerField', [], {'max_length': '45'}),
            'seq_run_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Sequencing_Run']"}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'srb.sequencing_run': {
            'GSE': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'GSM': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'Meta': {'object_name': 'Sequencing_Run'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mirror_track_group': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'modENCODE_id': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'release_status': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'seq_run_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'sequencing_center': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['srb']