from django.urls import path

from . import views


app_name = 'equipsmith_dev'
urlpatterns = [
	# path('', views.index, name='index'),
	path('book/', views.book_list, name='book_list'),
	path('book/add', views.book_edit, name='book_add'),
	path('book/mod/<int:book_id/', views.book_edit, name='book_mod'),
	path('book/del/<int:book_id/', views.book_del, name='book_del'),
]