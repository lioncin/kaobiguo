from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kaobiguo.views.home', name='home'),
    # url(r'^kaobiguo/', include('kaobiguo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'KBGMain.views.main'),
    url(r'^register/', 'Register.views.register'),
    url(r'^ajax/getCurrentHotMsgs/','Register.views.getCurrentHotMsgs'),
    url(r'^register/ajax/checkNameAndEmailExitst/','Register.views.checkNameAndEmailExitst'),
    
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )