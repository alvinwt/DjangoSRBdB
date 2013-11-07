from django.views.generic import DetailView
from .models import Read_alignment, Interval

from django_tables2 import RequestConfig, SingleTableMixin
import re
from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
import itertools

from tables import DetailTable
    
class IntervalDetailView(SingleTableMixin,DetailView):
    model= Interval
    table_class = DetailTable
    context_table_name = 'interval_detail'

    
    def get_table_data (self):
        table_data= Read_alignment.objects.filter(intervalName=self.object.NeatName)
        return table_data
    
    def get_seq(self):
        if Interval.objects.filter(read_alignment__intervalName=self.object.pk).exists():
            stt = self.object.start 
            stp = self.object.stop +20
        else:
            stt = self.object.start
            stp = self.object.stop
        #still hardcoded! needs to be static*
        for seq_record in SeqIO.parse('/home/alvin/Dropbox/FYP/Django/mysite/srb/media/dmel-3L-chromosome-r5.52.fasta','fasta'):
            seq = seq_record.seq
            seqInterval = str(seq[stt:stp])
            return seqInterval

    
            # rev_seq = seq_record.seq.reverse_complement()
            # if self.object.strand == '+':
               
            # else:
            #     seqInterval =  str(seq[stt:stp].reverse_complement())
            
    def get_msa(self):
        self = self.object                
        # read_list = Read_alignment.objects.filter(chr= self.chr, start__gte= self.start , stop__lte=self.stop)
        read_list=Read_alignment.objects.select_related().filter(intervalName=self.NeatName)
        string =""
        for i in read_list:
            reads = '%s \t\t %s\n' % (i.sequence, str(i.read_counts))
            spaces = int(i.start)-int(self.start)
            if spaces >= 1:
                string += spaces * ' ' + reads 
            else:
                string += reads
        return string

    def get_graph(self):
        self=self.object
        reads= Read_alignment.objects.filter(intervalName=self)
        cord = []
        data =[]
        index = []
        for i in reads:
            index.append(i.id)
            cord.append(i.start)
            cord.append(i.stop)
            ac =[int(i.start-self.start)*str(0),int(i.stop-i.start) *str(i.read_counts),int(self.stop-i.stop)*str(0)]
            data.append(list("".join(ac)))
        nt=sorted(cord)
        cords = range(self.start,self.stop)
        matrix = []
        for i in data:
            i=map(int,i)
            matrix.append(i)
        frame = pd.DataFrame(matrix,columns=cords, index=index )
        pile= frame.values.sum(axis=0)
        graph_list=[]
        for i in range(0,len(cords)):
            graph_list.append([cords[i],pile[i]])
        return graph_list

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
        context = super(IntervalDetailView,self).get_context_data(**kwargs)
        context['seq'] = self.get_seq()
        context['msa'] = self.get_msa()
        context['graph']= self.get_graph()
        return context
    
