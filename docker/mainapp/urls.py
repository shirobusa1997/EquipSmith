from django.urls import path

from mainapp import views


appname = "mainapp"
urlpatterns = [
	path('bstest', views.bstest, name='bstest'),
	path('', views.index, name='index'),
	path('top', views.top, name='top'),
	path('list', views.list, name='list'),
	path('createRecord/<int::id>', views.createRecord, name='createRecord')
	path('returnResource/<int::id>', views.returnResource, name='returnResource')
]