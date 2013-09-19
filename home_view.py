from django.views.generic import TemplateView
from django_tables2 import RequestConfig
from django.shortcuts import render
from tables import IntervalTable
from srb.models import Interval, IntervalFilter
from django.shortcuts import render_to_response


class HomeView(TemplateView):
    template_name = "srb/home.html"
    #html not written yet.

def Int_filter(request):
    f = IntervalFilter(request.GET, queryset=Interval.objects.all())
    return render_to_response('srb/int_data.html', {'filter': f})
    
def interval(request):
    intTable= IntervalTable(Interval.objects.all())
    RequestConfig(request).configure(intTable)
    return render(request,"srb/int_data.html",{'home_int':intTable})
