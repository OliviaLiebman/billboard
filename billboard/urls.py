from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as authviews


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^printName$', views.printName, name='printName'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='post_list'),
    url(r'^paste_post', views.post_list, name='save_post'),
    url(r'^login/$', authviews.login, name='login'),
    url(r'^logout/$', authviews.logout, {'next_page': '/'}, name='logout'),
]