from django.conf.urls import patterns, include, url

from partial_test.views import partial_test, PartialView, partial_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', partial_test, name='partial_test'),
    url(r'^function-based-partial-view/(?P<arg1>\d+)/(?P<arg2>\d+)/$',
        partial_view,
        name='function_based_partial_view'),
    url(r'^class-based-partial-view/(?P<arg1>\d+)/(?P<arg2>\d+)/$',
        PartialView.as_view(),
        name='class_based_partial_view'),
    url(r'^admin/', include(admin.site.urls)),
)
