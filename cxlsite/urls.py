from django.conf.urls import patterns, url
from login import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cxlsite.views.home', name='home'),
    # url(r'^cxlsite/', include('cxlsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^login/', views.login),
     url(r'^getin/',views.getin),
     url(r'getdata/',views.getdata),
     url(r'test/',views.test),

)
