### This is a model file for the Small RNA Biogenesis database. This will have the database modelling details. Whether blank=True, Null=True, ManyToManyField or ForeignKeys can be deliminated. 

from django.db import models
from django.db.models import Avg
from decimal import Decimal   


class Interval(models.Model):
    # mapped intervals and locations can be used to link to USCS genome browser
    chr= models.CharField(max_length=45)
    start= models.IntegerField(max_length=15)
    stop= models.IntegerField(max_length=15)
    NeatName= models.CharField(max_length=100,primary_key=True)
    IntervalSize= models.IntegerField(max_length=45)
    IntervalSerialNumber = models.IntegerField(max_length=45)
    Link= models.URLField(max_length=200)

    @property
    def interval (self):
        return '%s:%s,%s' %(self.chr,str(self.start+1),str(self.stop))

    def __unicode__(self):
        return u'%s:%s-%s' %(self.chr,str(self.start),str(self.stop))

class Library(models.Model):
    #library contains information about each library, called upon when needed for comparison.
    library_id = models.CharField(max_length=16,primary_key=True)
    description = models.CharField(max_length=255, blank=True)
    organism = models.CharField(max_length=45, blank=True)
    strain = models.CharField(max_length=45, blank=True)
    allele = models.CharField(max_length=45, blank=True)
    tissue = models.CharField(max_length=128, blank=True)
    target = models.CharField(max_length=45, blank=True)
    type =  models.CharField(max_length=45, blank=True)
    resolution =  models.CharField(max_length=45, blank=True)
    source_org =  models.CharField(max_length=45, blank=True)
    source_person = models.CharField(max_length=45, blank=True)
    five_prime_adapter_sequence = models.CharField(max_length=128, blank=True)
    three_prime_adapter_sequence = models.CharField(max_length=128, blank=True)
    multiplex_barcode_sequence =  models.CharField(max_length=45, blank=True)
    notes = models.TextField(max_length=500, blank=True)
    
    def __unicode__(self):
         return self.library_id
     
    class Meta:
         ordering = ['library_id']

class Sequencing_Run(models.Model):
    seq_run_id = models.CharField(max_length=16)
    sequencing_center = models.CharField(max_length=45)
    release_status = models.CharField(max_length=45, blank=True)
    GSM = models.CharField(max_length=45, blank=True)
    GSE = models.CharField(max_length=45, blank=True)
    modENCODE_id = models.CharField(max_length=45, blank=True)
    mirror_track_group = models.CharField(max_length=45, blank=True)
    
    def __unicode__(self):
        return u'%s %s' % (self.seq_run_id, self.sequencing_center)
    
class Library_Sequencing_Run(models.Model):
    library_id= models.ForeignKey(Library)
    seq_run_id= models.ForeignKey(Sequencing_Run)
    def __unicode__(self):
        return u'%s %s' % (self.library_id, self.seq_run_id)

class Genome_Build(models.Model):
    genome_build_id = models.CharField(max_length=45)

    def __unicode__(self):
        return self.genome_build_id

class PlusManager(models.Manager):
    def get_queryset(self):
        return super(PlusManager,self).get_queryset().filter(strand='+')

    
class MinusManager(models.Manager):
    def get_queryset(self):
        return super(MinusManager,self).get_queryset().filter(strand='-')
        
class Graph_Manager(models.Manager):
    def get_graph(self):
        if int(self.start)- 20 < 0:
            start = self.start
        else:
            start = int(self.start) - 20

            graph_query = Read_alignment.objects.get_queryset().filter(start__lte=int(start),stop__gte= int(self.stop)+50)    
            return graph_query.values_list 
        
class Read_alignment(models.Model):
    #library can be used as a foreign key to link libraries to read alignments
    library_id = models.ForeignKey(Library)
    sequence = models.CharField(max_length=150)
    read_counts = models.IntegerField(max_length=45)
    genomic_hits = models.IntegerField(max_length=45)
    chr = models.CharField(max_length=45)
    start = models.IntegerField(max_length=45)
    stop = models.IntegerField(max_length=45)
    strand = models.CharField(max_length=5, choices={('+','+'),('-','-')})
    normRead=models.DecimalField(max_digits=10,decimal_places=4)
    big2catrenormRPmirpre = models.DecimalField(max_digits=10, decimal_places=4,blank=True)
    AGO1IPoverTotalRNA = models.DecimalField(max_digits=10,decimal_places=4, blank = True)
    
    
    #"V063V0632renormRPmirpreadd" to "V066V0662renormRPmirpreadd" =normreads with diff headings for each lib?
    #aligned_interval = models.ForeignKey(Interval)
    # seq_run_id =  models.ForeignKey(Sequencing_Run)
    # genome_build_id = models.ForeignKey(Genome_Build)

    objects = models.Manager()
    aligned_objects = Graph_Manager()
    minus = MinusManager()
    plus = PlusManager()

    def __unicode__(self):
        return u'%s %s %s' % (self.chr, self.start, self.stop)
    
    # (read_counts/ genomic_hits) per million mirPrecursor Reads
    # consider pickling, or using celery for reducing lag / processing time
    # think how to code this dynamically. not hard coding.
    
    def normRead(self):
        ### wtCS = Read_alignment.objects.filter(library__contains=lib)
        wtCS_mapped = int(86837856) / 10^6
        normalized_count = (Decimal(self.read_counts) / Decimal(self.genomic_hits)) / wtCS_mapped
        return '%e' % (normalized_count)           
