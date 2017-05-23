
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
urlpatterns = [
   
    url(r'^$',views.home,name='home'),
    #url(r'^',social.apps.django_app.urls),
    #url('^oauth/', include('social.apps.django_app.urls', namespace='social')),
  

    #url(r'^accounts/',include('allauth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^$', 'django_social_app.views.login'),
     #url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login,name='login'),
    url(r'^forgot/$',views.forgot,name='forgot'),
    url(r'^reset/$',views.reset,name='reset'),
    url(r'^userpage/$',views.userpage,name='userpage'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^loginfb/$',views.loginfb,name='loginfb'),
    url(r'^privacy/$',views.privacy,name='loginfb'),



    #url(r'^create/$',views.create,name='create'),^address_edit/(\d+)/$
     #url(r'^edit/(\d+)/$',views.edit,name='edit'),

     
     #url(r'^delete/(\d+)/$',views.delete,name='delete'),
     #url(r'^update/$',views.update,name='update'),
]

