from django.shortcuts import render
from django.http import HttpResponse

from equipsmith_dev.models import Book

# Create your views here.

def book_list(request):
	# 書庫の一覧
	# return HttpResponse('書庫の一覧')
	books = Book.objects.all().order_by('id')
	return render(request, 'equipsmith_dev/book_list.html', {'books': books})


def book_edit(request, book_id=None):
	# 書庫の編集
	return HttpResponse('書庫の編集')


def book_del(request, book_id):
	# 書庫の削除
	return HttpResponse('書庫の削除')
# def index(request):
# 	return HttpResponse("ハロー・ワールド.")