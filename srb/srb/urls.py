from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< Updated upstream

from all_data_view import align
from home_view import HomeView
from detail_view import AlignDetailView
from search_view import  AlignRetrieveAPIView

=======
from rest_framework import routers
from all_data_view import align, view, align_filter
from home_view import interval, int_filter, search_form
from detail_view import AlignDetailView
from interval_detail_view import IntervalDetailView
from search_view import  AlignRetrieveAPIView, AlignViewSet
>>>>>>> Stashed changes

#pseudogene, remnant of old codes. for troubleshooting images, or matplotlib graph

from views import AlignListAPIView,LibraryListView, IntView,coordinate,showStaticImage, AlignListView
from srb.models import Library, Interval
from graph import plotResults

# linking using tables2 req url("") to pass third name arg.
# name used should be the class name to map to ind column or entry. 

admin.autodiscover()
<<<<<<< Updated upstream
urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                      url(r'^home/$',HomeView.as_view(),name='home'),
                      url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
                      url (r'^id/$',LibraryListView.as_view(),name='library_list'),
=======
router = routers.DefaultRouter()
router.register(r'boom', AlignViewSet)
urlpatterns = router.urls
urlpatterns += patterns('',
                       (r'^admin/', include(admin.site.urls)),
                      (r'^auth/', include('rest_framework.urls',
                                                 namespace='rest_framework')),
                      url(r'^id/$',LibraryListView.as_view(),name='library_list'),
>>>>>>> Stashed changes
                      url(r'^align/$',align,name="all_data"),                    
                      url(r'^(?P<pk>\d+)/align/graph<pk>.png$',plotResults,name='graph'),
                      url(r'^(?P<pk>\d+)/align/$', AlignDetailView.as_view(), name='AlignDetailView', ),
                      url(r'^(?P<pk>\d+)/align/$',showStaticImage),
                      url(r'^api/$', AlignListAPIView.as_view(), name='list'),
<<<<<<< Updated upstream
                      url(r'^api/(?P<pk>\d+)/$', AlignRetrieveAPIView.as_view(), name='retrieve'),
                      url(r'^', include('cms.urls')),
)

=======
                      url(r'^interval/$',interval, name='interval'),
                      url(r'^(?P<pk>[0-9A-Za-z-_.//:]+)/interval/$', IntervalDetailView.as_view(), name='IntervalDetailView', ),
                      url(r'^interval/search/$',int_filter,name='int_filter'),
                       url(r'^align/search/$',align_filter,name='align_filter'),
# url(r'^interval/$',search_form),
url(r'^api/$', AlignRetrieveAPIView.as_view(), name='retrieve'),
#url(r'^api-detail/$', AlignViewSet.as_view(), name='align-detail'),
url(r'^', include('cms.urls')),                   
)


>>>>>>> Stashed changes
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
