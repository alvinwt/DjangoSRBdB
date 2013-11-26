import django_tables2 as tables
from django_tables2 import SingleTableMixin
from django_tables2.utils import A
from django.db.models import Avg
from models import Interval, Read_alignment

class IntervalTable(tables.Table):
     NeatName = tables.LinkColumn('IntervalDetailView',args=[A('pk')])
     class Meta:
        model = Interval
        attrs = {"class":"paleblue"}
        sequence =('IntervalSerialNumber','NeatName', 'chr','start','stop','IntervalSize','Link')
        order_by = ('start',)
        exclude =('Structure',)
 # link column. name = " ", " " = AlignDetailView 
 
class AlignTable(tables.Table):
    #id= tables.CheckBoxColumn()
    # table cannot be sorted by normRead
    # intervalName = tables.Column(order_by=('intervalName'))
    id = tables.LinkColumn('AlignDetailView',args=[A('pk')])

    class Meta:
        model = Read_alignment
        sequence = ('id','chr','start','stop','sequence','read_counts','genomic_hits','strand','normReads','intervalName',)
        attrs = {"class":"paleblue"}
        exclude = ('normRead',)
        order_by = ('-intervalName','strand')
        

class DetailTable(SingleTableMixin,tables.Table):
    class Meta:
        model = Read_alignment
        sequence = ('id','chr','start','stop','read_counts','genomic_hits','strand','normReads','intervalName','sequence')
        attrs = {"class":"paleblue"}
        fields=('id','chr','start','stop','read_counts','genomic_hits','strand','normReads','intervalName','sequence')
       

#table_data = (Read_alignment.objects.get(id='127'))
#class IntervalDetailTable(SingleTableMixin,tables.Table):
