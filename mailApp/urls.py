from django.conf.urls import url

urlpatterns = [
   
    url(r'^(?P<mail_id>[0-9]+)/$', 'mailApp.views.contact', name='contact'),
    # url(r'^mailApp/', include('mailApp.urls', namespace="mailApp")),
]