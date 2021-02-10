from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^new/profile$', views.add_profile, name='edit'),
    url(r'^myprofile$', views.my_profile, name='myprofile'),
    url(r'^new/upload/$', views.add_neighborhood, name='upload'),
    url(r'^hood/(\d+)/$', views.neighborhood, name='hood'),
    url(r'^addbusiness/(\d+)/$', views.add_business, name = 'addbusiness'),
    url(r'^addpost/(\d+)/$', views.add_post, name = 'addpost'),
    url(r'^search/$',views.search_business, name = 'search'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)