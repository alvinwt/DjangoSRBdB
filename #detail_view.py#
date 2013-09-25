from django.views.generic import DetailView
from srb.models import Read_alignment

import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Align.Applications import ClustalOmegaCommandline

import numpy as np
from numpy import array
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from graph import plotResults

from django.shortcuts import render
from django_tables2 import RequestConfig, SingleTableMixin
from tables import AlignTable, DetailTable

class AlignDetailView(SingleTableMixin,DetailView):
    model = Read_alignment
    table_class = DetailTable
    context_table_name = 'detail' 
    
    def get_sum(self):
        sum = self.object.read_counts +self.object.read_counts
        return sum

    def get_seq(self):
        stt = self.object.start 
        stp = self.object.stop +50

        for seq_record in SeqIO.parse('/home/alvin/Dropbox/FYP/Django/mysite/srb/media/dmel-3L-chromosome-r5.52.fasta','fasta'):
            seq = seq_record.seq
            # rev_seq = seq_record.seq.reverse_complement()
            if self.object.strand == '+':
                seqInterval = str(seq[stt:stp])
            else:
                seqInterval =  str(seq[stt:stp].reverse_complement())
            return seqInterval
            
    def get_mapping(self):
        #get sequences that are in the region, currently hard coded, can be done with intervals specified.
        dob= self.object
        if int(dob.start) - 20 <= 0:
           start = int(dob.start)
        else:
            start = int(dob.start-50)
        stop = dob.stop + 20 
        seq = Read_alignment.objects.filter(chr=dob.chr,strand=dob.strand, start__gte=start,stop__lte=stop).values_list('id','sequence')
        seqArray= array(seq)
        s = []
        for i in seqArray:
            s.append(">"+ i[0] + "\n"+ i[1] +"\n")
        clustalo_cline= ClustalOmegaCommandline(infile='-')
        stdout,stderr=clustalo_cline("".join(s))
        stdout = re.sub(r'(?<=\d)\n(\w)',' ',stdout)
        stdout = re.sub(r'>', '\n' ,stdout)
        return stdout

    def get_read_counts(self):
        dob= self.object
        if int(dob.start) - 20 <= 0:
           start = int(dob.start)
        else:
            start = int(dob.start-20)
        stop = dob.stop + 20 
        count = Read_alignment.objects.filter(chr=dob.chr,strand=dob.strand, start__gte=start,stop__lte=stop).values_list('start','stop','read_counts')
        return count
 
    def get_context_data(self, **kwargs):
        context = super(AlignDetailView,self).get_context_data(**kwargs)
        context['sum'] = self.get_sum()
        context['seq'] = self.get_seq()
        context['msa'] = self.get_mapping()
        context['cts'] = self.get_read_counts()
        return context

