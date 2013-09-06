from django.shortcuts import render
from srb.tables import AlignTable
from django_tables2 import RequestConfig
from srb.models import Read_alignment

#page for table with alignments, intervals of all data

def align(request):
    table= AlignTable(Read_alignment.objects.all().order_by('strand','id'))
    RequestConfig(request).configure(table)
    return render(request,"srb/align_data.html",{'all_data':table})
