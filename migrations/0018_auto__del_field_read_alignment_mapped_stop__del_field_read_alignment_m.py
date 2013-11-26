# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Read_alignment.mapped_stop'
        db.delete_column(u'srb_read_alignment', 'mapped_stop')

        # Deleting field 'Read_alignment.mapped_start'
        db.delete_column(u'srb_read_alignment', 'mapped_start')

        # Deleting field 'Read_alignment.mapped_chr'
        db.delete_column(u'srb_read_alignment', 'mapped_chr')

        # Adding field 'Read_alignment.chr'
        db.add_column(u'srb_read_alignment', 'chr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45),
                      keep_default=False)

        # Adding field 'Read_alignment.start'
        db.add_column(u'srb_read_alignment', 'start',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45),
                      keep_default=False)

        # Adding field 'Read_alignment.stop'
        db.add_column(u'srb_read_alignment', 'stop',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Read_alignment.mapped_stop'
        raise RuntimeError("Cannot reverse this migration. 'Read_alignment.mapped_stop' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Read_alignment.mapped_start'
        raise RuntimeError("Cannot reverse this migration. 'Read_alignment.mapped_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Read_alignment.mapped_chr'
        raise RuntimeError("Cannot reverse this migration. 'Read_alignment.mapped_chr' and its values cannot be restored.")
        # Deleting field 'Read_alignment.chr'
        db.delete_column(u'srb_read_alignment', 'chr')

        # Deleting field 'Read_alignment.start'
        db.delete_column(u'srb_read_alignment', 'start')

        # Deleting field 'Read_alignment.stop'
        db.delete_column(u'srb_read_alignment', 'stop')


    models = {
        u'srb.genome_build': {
            'Meta': {'object_name': 'Genome_Build'},
            'genome_build_id': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'srb.library': {
            'Meta': {'ordering': "['library_id']", 'object_name': 'Library'},
            'allele': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'library_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'multiplex_barcode_sequence': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
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
        u'srb.location': {
            'Meta': {'object_name': 'Location'},
            'UCSC_mirror': ('django.db.models.fields.CharField', [], {'max_length': '45', 'primary_key': 'True'}),
            'big2catnormRead': ('django.db.models.fields.IntegerField', [], {'max_length': '50', 'blank': 'True'}),
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'start': ('django.db.models.fields.IntegerField', [], {'max_length': '15'}),
            'stop': ('django.db.models.fields.IntegerField', [], {'max_length': '15'})
        },
        u'srb.read_alignment': {
            'Meta': {'object_name': 'Read_alignment'},
            'chr': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'genome_build_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Genome_Build']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapped_coordinate': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['srb.Location']"}),
            'mapped_strand': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'number_genomic_hits': ('django.db.models.fields.FloatField', [], {'max_length': '45'}),
            'read_alignment_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'read_counts': ('django.db.models.fields.IntegerField', [], {'max_length': '45'}),
            'seq_run_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Sequencing_Run']"}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'stop': ('django.db.models.fields.CharField', [], {'max_length': '45'})
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