# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Library.location'
        db.add_column(u'srb_library', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['srb.Location']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Library.location'
        db.delete_column(u'srb_library', 'location_id')


    models = {
        u'srb.genome_build': {
            'Meta': {'object_name': 'Genome_Build'},
            'genome_build_id': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'srb.library': {
            'Meta': {'ordering': "['library_id']", 'object_name': 'Library'},
            'allele': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'library_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Location']"}),
            'multiplex_barcode_sequence': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'organism': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'resolution': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'source_org': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'source_person': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'strain': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'tissue': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'srb.library_sequencing_run': {
            'Meta': {'object_name': 'Library_Sequencing_Run'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'library_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Library']"}),
            'seq_run_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Sequencing_Run']"})
        },
        u'srb.location': {
            'Meta': {'object_name': 'Location'},
            'UCSC_GB_mirror': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'big2catnormRead': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {'max_length': '15'}),
            'stop': ('django.db.models.fields.IntegerField', [], {'max_length': '15'})
        },
        u'srb.read_alignment': {
            'Meta': {'object_name': 'Read_alignment'},
            'NormRPM': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'NormReads': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'RPM': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'genome_build_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Genome_Build']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapped_chr': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mapped_interval': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Location']"}),
            'mapped_start': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mapped_stop': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mapped_strand': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'number_genomic_hits': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'read_alignment_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'read_counts': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'seq_run_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Sequencing_Run']"}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'srb.sequencing_run': {
            'GSE': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'GSM': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'Meta': {'object_name': 'Sequencing_Run'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mirror_track_group': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'modENCODE_id': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'release_status': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'seq_run_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'sequencing_center': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['srb']