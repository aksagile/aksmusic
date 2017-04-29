from django.conf.urls import url
from . import views

app_name = 'aksmusic'


# Create your views here.
urlpatterns = [
    url(r'^$', views.index, name = 'index' ),
    url(r'^register/$', views.UserFormView.as_view(), name = 'register' ),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name ='detail'),
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name ='favorite'),
    ]
