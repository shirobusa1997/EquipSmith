from django.urls import path

from mainapp import views


appname = "mainapp"
urlpatterns = [
	path('bstest', views.bstest, name='bstest'),
	path('', views.index, name='index'),
]