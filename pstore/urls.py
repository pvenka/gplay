from django.conf.urls import url
from pstore import views

urlpatterns = [
	 url(r'^search_results/$', views.search_results,name='search_results'),
	 
	 url(r'^test/$', views.test, name='test'),
	  ]


