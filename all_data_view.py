from django.shortcuts import render
from io import BytesIO
from srb.tables import AlignTable
from django_tables2 import RequestConfig
from srb.models import Read_alignment
from reportlab.pdfgen import canvas
from django.http import HttpResponse

#page for table with alignments, intervals of all data

def align(request):
    table= AlignTable(Read_alignment.objects.all().order_by('strand','id'))
    RequestConfig(request).configure(table)
    return render(request,"srb/align_data.html",{'all_data':table})

def view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100,100,"text.")
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
