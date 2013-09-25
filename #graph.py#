from django.shortcuts import render, get_object_or_404,render_to_response
from django.template import RequestContext
from django.views.generic.detail import BaseDetailView
from srb.models import Library_Sequencing_Run, Library, Interval, Read_alignment
from srb.tables import CoordinateTable, AlignTable
import os
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.http import Http404,  HttpResponse
from numpy.random import normal
import matplotlib.pyplot as plt

import numpy as np
from numpy import array
import pylab as p

def plotResults(request,pk):
    pts = Read_alignment.objects.get(pk=pk)
    
    a = int(pts.start)
    b = int(pts.stop)
    c = int(pts.read_counts)
    counts = Read_alignment.objects.filter(chr=pts.chr,strand=pts.strand,start__gte=a,stop__lte=b+100).values_list('read_counts',flat=True)

    x1= range(a,b)
    y1= [c,c]
    x = [1,2,3,4,5]
    y = [2,3,4,8,9]
    fig=plt.figure()
    ax= fig.add_subplot(111)
    ax.set_xlim(right=50)
    ax.step(counts,'-', label='')
    # ay= fig.add_subplot(312)
    # ay.set_xlim(right=50)
    # ay.step(w,z,'r-',label='')
    # az= fig.add_subplot(313)
    # az.set_xlim(right=50)
    # az.step(v,z,'g-',label='')
    canvas = FigureCanvas(fig)
    response= HttpResponse(mimetype='image/jpg')
    #response['Content-Disposition']= 'graph.svg'
    plt.savefig("graph.svg")
    canvas.print_png(response)
    return response
