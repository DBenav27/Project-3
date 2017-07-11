# main_app/urls.py
from django.conf.urls import url
from main_app import views
from views import index
from views import show
from views import post_treasure
from django.views.static import serve
from . import views


urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', views.show, name="show"),
    url(r'^post_url/$', views.post_treasure, name="post_treasure"),
    url(r'^$', views.index),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^like_treasure/$', views.like_treasure, name='like_treasure')
]

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve,
#             {'document_root': settings.MEDIA_ROOT,}),
#         ]
