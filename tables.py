import django_tables2 as tables
from django_tables2 import SingleTableMixin
from django_tables2.utils import A
from django.db.models import Avg
from models import Interval, Read_alignment

class IntervalTable(tables.Table):
    class Meta:
        model = Interval
        attrs = {"class":"paleblue"}
        sequence =('IntervalSerialNumber','NeatName', 'chr','start','stop','IntervalSize','Link')
 # link column. name = " ", " " = AlignDetailView 
 
class AlignTable(tables.Table):
    #id= tables.CheckBoxColumn()
    # table cannot be sorted by normRead
    normRead = tables.Column(order_by=('read_counts','genomic_hits'))
    id = tables.LinkColumn('AlignDetailView',args=[A('pk')])

    class Meta:
        model = Read_alignment
        sequence = ('id','chr','start','stop','sequence','read_counts','genomic_hits','strand','normReads','intervalName',)
        attrs = {"class":"paleblue"}
        exclude = ('normRead',)
        

class DetailTable(SingleTableMixin,tables.Table):
    name = tables.Column()
    data = {}
    
