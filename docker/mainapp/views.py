from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from mainapp.models import Equipments

# Create your views here.
def index(request):
	# return HttpResponse("EQUIP SMITH BLANK PAGE")
	return redirect("bstest")


def bstest(request):
	equipments_list = Equipments.objects.all()
	# messages.info(request, '%s' % equipments_list.count())
	return render(request, 'bstest.html')

def top(request):
	equipments_list = Equipments.objects.all()
	params = {'message': 'メンバーの一覧', 'equipments_list': equipments_list}
	return render(request, 'mainapp/top.html', params)
	
def list(request):
	return render(request, 'mainapp/list.html')
	