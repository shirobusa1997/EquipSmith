from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import get_user_model
from mainapp.models import Equipments, Records

# Create your views here.
def index(request):
	# return HttpResponse("EQUIP SMITH BLANK PAGE")
	return redirect("bstest")


def bstest(request):
	equipments_list = Equipments.objects.all()
	# messages.info(request, '%s' % equipments_list.count())
	return render(request, 'bstest.html')

def top(request):
	context = ['green', 'yellow', 'orange', 'red']
	equipments_list = Equipments.objects.all()
	personal_record = Records.objects.filter(Q(userid=request.user) & (Q(status='green') | Q(status='blue')))
	params = {
				'message': 'メンバーの一覧',
				'equipments_list': equipments_list,
				'personal_record': personal_record,
				'context': context,
			 }
	return render(request, 'mainapp/top.html', params)
	
def list(request):
	equipments_list = Equipments.objects.all()
	params = {
				'message': '利用可能な備品一覧',
				'available_equipments': 'equipments_list',
			 }
	return render(request, 'mainapp/list.html', params)

def createRecord(request):
	
	return HttpResponseRedirect(reverse('list'))

def returnResource(request):

	return HttpResponseRedirect(reverse('top'))