from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from all_data_view import align
from home_view import HomeView
from detail_view import AlignDetailView
from search_view import  AlignRetrieveAPIView


#pseudogene, remnant of old codes. for troubleshooting images, or matplotlib graph

from views import AlignListAPIView,LibraryListView, IntView,coordinate,showStaticImage, AlignListView
from srb.models import Library, Interval
from graph import plotResults

# linking using tables2 req url("") to pass third name arg.
# name used should be the class name to map to ind column or entry. 

admin.autodiscover()
urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                      url(r'^home/$',HomeView.as_view(),name='home'),
                      url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
                      url (r'^id/$',LibraryListView.as_view(),name='library_list'),
                      url(r'^align/$',align,name="all_data"),                    
                      url(r'^(?P<pk>\d+)/align/graph<pk>.png$',plotResults,name='graph'),
                      url(r'^(?P<pk>\d+)/align/$', AlignDetailView.as_view(), name='AlignDetailView', ),
                      url(r'^(?P<pk>\d+)/align/$',showStaticImage),
                      url(r'^api/$', AlignListAPIView.as_view(), name='list'),
                      url(r'^api/(?P<pk>\d+)/$', AlignRetrieveAPIView.as_view(), name='retrieve'),
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
    # (r'^coordinate/$', coordinate),
    # (r'^lalign/$',AlignListView.as_view()),)
    # (r'^staticImage.png$', showStaticImage),
    #  url(r'^balign/$',plotResults),
