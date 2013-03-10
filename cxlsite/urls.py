from django.conf.urls.defaults import *
from cxlsite.views import hello,current_datetime,hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^hello/$',hello),
                       ('^time/$',current_datetime),
                       (r'^time/plus/(\d{1,2})/$',hours_ahead),
    # Examples:
    # url(r'^$', 'cxlsite.views.home', name='home'),
    # url(r'^cxlsite/', include('cxlsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
