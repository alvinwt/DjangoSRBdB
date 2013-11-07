import django_tables2 as tables
from django_tables2 import SingleTableMixin
from django_tables2.utils import A
from django.db.models import Avg
from models import Interval, Read_alignment

<<<<<<< Updated upstream
class CoordinateTable(tables.Table):
    #normRead=tables.Column()
    class Meta:
        model = Interval
        attrs = {"class":"paleblue"}
=======
class IntervalTable(tables.Table):
    # NeatName = tables.LinkColumn('IntervalDetailView',args=[A('pk')])
     class Meta:
        model = Interval
        attrs = {"class":"paleblue"}
        sequence =('IntervalSerialNumber','NeatName', 'chr','start','stop','IntervalSize','Link')
        order_by = ('start',)
>>>>>>> Stashed changes
 # link column. name = " ", " " = AlignDetailView 
 
class AlignTable(tables.Table):
    #id= tables.CheckBoxColumn()
    # table cannot be sorted by normRead
<<<<<<< Updated upstream
    normRead = tables.Column(orderable=False)
=======
    # intervalName = tables.Column(order_by=('intervalName'))
>>>>>>> Stashed changes
    id = tables.LinkColumn('AlignDetailView',args=[A('pk')])

    class Meta:
        model = Read_alignment
<<<<<<< Updated upstream
        sequence = ('id','chr','start','stop','sequence','read_counts','genomic_hits','strand','library_id')
=======
        sequence = ('id','chr','start','stop','sequence','read_counts','genomic_hits','strand','normReads','intervalName',)
>>>>>>> Stashed changes
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
