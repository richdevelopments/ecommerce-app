{"filter":false,"title":"urls.py","tooltip":"/accounts/urls.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import index, register, profile, logout, login","","urlpatterns = [","    url(r'^register/$', register, name='register'),","    url(r'^profile/$', profile, name='profile'),","    url(r'^logout/$', logout, name='logout'),","    url(r'^login/$', login, name='login'),","    url(r'^password-reset/', include(urls_reset)),","]"],"id":2},{"start":{"row":0,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from . import urls_reset","from .views import index, register, profile, logout, login","","urlpatterns = [","    url(r'^register/$', register, name='register'),","    url(r'^profile/$', profile, name='profile'),","    url(r'^logout/$', logout, name='logout'),","    url(r'^login/$', login, name='login'),","    url(r'^password-reset/', include(urls_reset)),","]"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":1},"end":{"row":10,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564067403160,"hash":"24d9562b3f60b7c396c136f09c625abe655faab0"}