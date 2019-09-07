from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def book_list(request):
	# 書庫の一覧
	return HttpResponse('書庫の一覧')


def bool_edit(request, book_id=None):
	# 書庫の編集
	return HttpResponse('書庫の編集')


def bool_del(request, book_id):
	# 書庫の削除
	return HttpResponse('書庫の削除')
# def index(request):
# 	return HttpResponse("ハロー・ワールド.")