# main_app/urls.py
from django.conf.urls import url
from main_app import views
from views import dates, index
from views import show
from views import post_treasure
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', views.show, name="show"),
    url(r'^post_url/$', views.post_treasure, name="post_treasure"),
    url(r'^$', views.index),
    url(r'^profiles/$', views.dates, name="dates"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^like_treasure/$', views.like_treasure, name='like_treasure'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
