from django.conf.urls.defaults import *

from cas_consumer.views import *

urlpatterns = patterns('',
    (r'^login/', login),
    (r'^logout/', logout),
)
