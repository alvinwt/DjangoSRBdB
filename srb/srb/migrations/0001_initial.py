# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Library'
        db.create_table(u'srb_library', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('library_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('organism', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('strain', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('allele', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('tissue', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('resolution', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('source_org', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('source_person', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('multiplex_barcode_sequence', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'srb', ['Library'])

        # Adding model 'Sequencing_Run'
        db.create_table(u'srb_sequencing_run', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq_run_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('sequencing_center', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('release_status', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('GSM', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('GSE', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('modENCODE_id', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('mirror_track_group', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'srb', ['Sequencing_Run'])

        # Adding model 'Library_Sequencing_Run'
        db.create_table(u'srb_library_sequencing_run', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('library_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Library'])),
            ('seq_run_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Sequencing_Run'])),
        ))
        db.send_create_signal(u'srb', ['Library_Sequencing_Run'])

        # Adding model 'Genome_Build'
        db.create_table(u'srb_genome_build', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genome_build_id', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'srb', ['Genome_Build'])

        # Adding model 'Location'
        db.create_table(u'srb_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('big2catnormRead', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
            ('chr', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('start', self.gf('django.db.models.fields.IntegerField')(max_length=15)),
            ('stop', self.gf('django.db.models.fields.IntegerField')(max_length=15)),
            ('UCSC_GB_mirror', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'srb', ['Location'])

        # Adding model 'Read_alignment'
        db.create_table(u'srb_read_alignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('read_alignment_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('seq_run_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Sequencing_Run'])),
            ('genome_build_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Genome_Build'])),
            ('sequence', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('read_counts', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('RPM', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('NormRPM', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('NormReads', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('mapped_chr', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('mapped_start', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('mapped_stop', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('mapped_strand', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('mapped_interval', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Location'])),
            ('number_genomic_hits', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'srb', ['Read_alignment'])


    def backwards(self, orm):
        # Deleting model 'Library'
        db.delete_table(u'srb_library')

        # Deleting model 'Sequencing_Run'
        db.delete_table(u'srb_sequencing_run')

        # Deleting model 'Library_Sequencing_Run'
        db.delete_table(u'srb_library_sequencing_run')

        # Deleting model 'Genome_Build'
        db.delete_table(u'srb_genome_build')

        # Deleting model 'Location'
        db.delete_table(u'srb_location')

        # Deleting model 'Read_alignment'
        db.delete_table(u'srb_read_alignment')


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