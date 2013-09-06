# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'srb_location', (
            ('big2catnormRead', self.gf('django.db.models.fields.IntegerField')(max_length=50, blank=True)),
            ('chr', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('start', self.gf('django.db.models.fields.IntegerField')(max_length=15)),
            ('stop', self.gf('django.db.models.fields.IntegerField')(max_length=15)),
            ('UCSC_mirror', self.gf('django.db.models.fields.CharField')(max_length=45, primary_key=True)),
        ))
        db.send_create_signal(u'srb', ['Location'])

        # Adding model 'Library'
        db.create_table(u'srb_library', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('library_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('organism', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('strain', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('allele', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('tissue', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('target', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('resolution', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('source_org', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('source_person', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('multiplex_barcode_sequence', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal(u'srb', ['Library'])

        # Adding model 'Sequencing_Run'
        db.create_table(u'srb_sequencing_run', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq_run_id', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('sequencing_center', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('release_status', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('GSM', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('GSE', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('modENCODE_id', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('mirror_track_group', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
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

        # Adding model 'Read_alignment'
        db.create_table(u'srb_read_alignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mapped_coordinate', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['srb.Location'], unique=True)),
            ('seq_run_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Sequencing_Run'])),
            ('genome_build_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['srb.Genome_Build'])),
            ('sequence', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('read_counts', self.gf('django.db.models.fields.IntegerField')(max_length=45)),
            ('avg_counts', self.gf('django.db.models.fields.FloatField')(max_length=45, null=True)),
            ('mapped_strand', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('mapped_interval', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('number_genomic_hits', self.gf('django.db.models.fields.FloatField')(max_length=45)),
        ))
        db.send_create_signal(u'srb', ['Read_alignment'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'srb_location')

        # Deleting model 'Library'
        db.delete_table(u'srb_library')

        # Deleting model 'Sequencing_Run'
        db.delete_table(u'srb_sequencing_run')

        # Deleting model 'Library_Sequencing_Run'
        db.delete_table(u'srb_library_sequencing_run')

        # Deleting model 'Genome_Build'
        db.delete_table(u'srb_genome_build')

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
            'avg_counts': ('django.db.models.fields.FloatField', [], {'max_length': '45', 'null': 'True'}),
            'genome_build_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['srb.Genome_Build']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapped_coordinate': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['srb.Location']", 'unique': 'True'}),
            'mapped_interval': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
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