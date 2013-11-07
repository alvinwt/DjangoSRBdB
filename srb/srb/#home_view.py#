from django.views.generic import TemplateView
from django_tables2 import RequestConfig
from django.shortcuts import render
from tables import IntervalTable, AlignTable
from srb.models import Interval, IntervalFilter,Read_alignment, AlignFilter
from django.shortcuts import render_to_response
from forms import MyModelForm

def int_filter(request):
    fil = IntervalFilter(request.GET, queryset = Interval.objects.select_related().all())
    f= IntervalTable(fil.qs)
    RequestConfig(request).configure(f)
    return render(request,'srb/filter.html', {'f': f, 'fil':fil})

def interval(request):
    intTable= IntervalTable(Interval.objects.all())
    RequestConfig(request).configure(intTable)
    return render(request,"srb/int_data.html",{'home_int':intTable})

def search_form(request):
    if request.method == 'GET':
        form = MyModelForm(request.GET)
        if form.is_valid():
            return render(request,'srb/int_data.html')
        else:
            return "shit darn it"

        # class HomeView(TemplateView):
#     template_name = "srb/home.html"
#     #html not written yet
