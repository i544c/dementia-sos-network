from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
]
