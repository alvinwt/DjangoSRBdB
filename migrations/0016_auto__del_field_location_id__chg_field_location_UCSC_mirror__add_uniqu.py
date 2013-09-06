# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Location.id'
        db.delete_column(u'srb_location', u'id')


        # Changing field 'Location.UCSC_mirror'
        db.alter_column(u'srb_location', 'UCSC_mirror', self.gf('django.db.models.fields.CharField')(max_length=45, primary_key=True))
        # Adding unique constraint on 'Location', fields ['UCSC_mirror']
        db.create_unique(u'srb_location', ['UCSC_mirror'])

        # Deleting field 'Read_alignment.NormRPM'
        db.delete_column(u'srb_read_alignment', 'NormRPM')

        # Deleting field 'Read_alignment.mapped_interval'
        db.delete_column(u'srb_read_alignment', 'mapped_interval')

        # Deleting field 'Read_alignment.NormReads'
        db.delete_column(u'srb_read_alignment', 'NormReads')

        # Deleting field 'Read_alignment.RPM'
        db.delete_column(u'srb_read_alignment', 'RPM')


        # Changing field 'Read_alignment.read_counts'
        db.alter_column(u'srb_read_alignment', 'read_counts', self.gf('django.db.models.fields.IntegerField')(max_length=45))

        # Changing field 'Read_alignment.number_genomic_hits'
        db.alter_column(u'srb_read_alignment', 'number_genomic_hits', self.gf('django.db.models.fields.FloatField')(max_length=45))

        # Changing field 'Read_alignment.sequence'
        db.alter_column(u'srb_read_alignment', 'sequence', self.gf('django.db.models.fields.CharField')(max_length=150))

    def backwards(self, orm):
        # Removing unique constraint on 'Location', fields ['UCSC_mirror']
        db.delete_unique(u'srb_location', ['UCSC_mirror'])


        # User chose to not deal with backwards NULL issues for 'Location.id'
        raise RuntimeError("Cannot reverse this migration. 'Location.id' and its values cannot be restored.")

        # Changing field 'Location.UCSC_mirror'
        db.alter_column(u'srb_location', 'UCSC_mirror', self.gf('django.db.models.fields.CharField')(max_length=45))

        # User chose to not deal with backwards NULL issues for 'Read_alignment.NormRPM'
        raise RuntimeError("Cannot reverse this migration. 'Read_alignment.NormRPM' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Read_alignment.mapped_interval'
        raise RuntimeError("Cannot reverse this migration. 'Read_alignment.mapped_interval' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Read_alignment.NormReads'
        raise RuntimeError("Cannot reverse this migration. 'Read_alignment.NormReads' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Read_alignment.RPM'
        raise RuntimeError("Cannot reverse this migration. 'Read_alignment.RPM' and its values cannot be restored.")

        # Changing field 'Read_alignment.read_counts'
        db.alter_column(u'srb_read_alignment', 'read_counts', self.gf('django.db.models.fields.CharField')(max_length=45))

        # Changing field 'Read_alignment.number_genomic_hits'
        db.alter_column(u'srb_read_alignment', 'number_genomic_hits', self.gf('django.db.models.fields.CharField')(max_length=45))

        # Changing field 'Read_alignment.sequence'
        db.alter_column(u'srb_read_alignment', 'sequence', self.gf('django.db.models.fields.CharField')(max_length=45))

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
            'genome_build_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Genome_Build']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapped_chr': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mapped_start': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mapped_stop': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'mapped_strand': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'number_genomic_hits': ('django.db.models.fields.FloatField', [], {'max_length': '45'}),
            'read_alignment_id': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'read_counts': ('django.db.models.fields.IntegerField', [], {'max_length': '45'}),
            'seq_run_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Sequencing_Run']"}),
            'sequence': ('django.db.models.fields.CharField', [], {'max_length': '150'})
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