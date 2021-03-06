from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from all_data_view import align, view, align_filter
from home_view import interval, int_filter, search_form
from detail_view import AlignDetailView
from interval_detail_view import IntervalDetailView
from search_view import  AlignRetrieveAPIView, AlignViewSet

import warnings
warnings.simplefilter('error', DeprecationWarning)
#pseudogene, remnant of old codes. for troubleshooting images, or matplotlib graph

from views import AlignListAPIView,LibraryListView, IntView,coordinate,showStaticImage, AlignListView
from srb.models import Library, Interval
from graph import plotResults

# linking using tables2 req url("") to pass third name arg.
# name used should be the class name to map to ind column or entry. 

admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'boom', AlignViewSet)
urlpatterns = router.urls
urlpatterns += patterns('',
                       (r'^admin/', include(admin.site.urls)),
                      (r'^auth/', include('rest_framework.urls',
                                                 namespace='rest_framework')),
                      url(r'^id/$',LibraryListView.as_view(),name='library_list'),
                      url(r'^align/$',align,name="all_data"),                    
                      url(r'^(?P<pk>\d+)/align/graph<pk>.png$',plotResults,name='graph'),
                      url(r'^/balign/$', view, name="align_view"),
                      url(r'^(?P<pk>\d+)/align/$', AlignDetailView.as_view(), name='AlignDetailView', ),
                      url(r'^api/$', AlignListAPIView.as_view(), name='list'),
                      url(r'^interval/$',interval, name='interval'),
                      url(r'^(?P<pk>[0-9A-Za-z-_.//:]+)/interval/$', IntervalDetailView.as_view(), name='IntervalDetailView', ),
                      url(r'^interval/search/$',int_filter,name='int_filter'),
                       url(r'^align/search/$',align_filter,name='align_filter'),
# url(r'^interval/$',search_form),
url(r'^api/$', AlignRetrieveAPIView.as_view(), name='retrieve'),
#url(r'^api-detail/$', AlignViewSet.as_view(), name='align-detail'),
url(r'^', include('cms.urls')),                   
)


if settings.DEBUG:
    urlpatterns += patterns('',
                           (r'^debug/$','debug'),
     )
# Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # # patterns can be added tgt '+=' v useful for diff patterns
    # urlpatterns += patterns('',
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^lalign/$',AlignListView.as_view()),)
    # (r'^staticImage.png$', showStaticImage),
    #  url(r'^balign/$',plotResults),
