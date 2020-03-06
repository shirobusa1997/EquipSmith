from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from equipsmith_dev.models import Book
from equipsmith_dev.forms import BookForm

# Create your views here.

from mainapp.models import Equipments

# Create your views here.
def index(request):
	return render(request, 'equipsmith_dev/book_list.html')
	# return HttpResponse("EQUIP SMITH BLANK PAGE")
	# return redirect("bstest")

def bstest(request):
	equipments_list = Equipments.objects.all()
	return render(request, 'equipsmith_dev/book_list.html')

def book_list(request):
	# 書庫の一覧
	# return HttpResponse('書庫の一覧')
	books = Book.objects.all().order_by('id')
	return render(request, 'equipsmith_dev/book_list.html', {'books': books})


def book_edit(request, book_id=None):
	# 書庫の編集
	if book_id:
		book = get_object_or_404(Book, pk=book_id)
	else:
		book = Book()

	if request.method == 'POST':
		form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
		if form.is_valid():    # フォームのバリデーション
			book = form.save(commit=False)
			book.save()
			return redirect('equipsmith_dev:book_list')
	else:    # GET の時
		form = BookForm(instance=book)  # book インスタンスからフォームを作成

	return render(request, 'equipsmith_dev/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
	# 書庫の削除
	book = get_object_or_404(book, pk=book_id)
	book.delete()
	return redirect('equipsmith_dev:book_list')