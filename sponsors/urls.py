from django.conf.urls import url
from .views import list_sponsors, view_sponsor

urlpatterns = [
    url(r'^$', list_sponsors, name='sponsors_list_sponsors'),
    url(r'^(?P<slug>[-a-zA-Z0-9]+)/$', view_sponsor, name='sponsors_view_sponsor'),
]
